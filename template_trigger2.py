#トリガ機能を用いたシナリオ(衝突あり、評価用)
import logging
import threading
import time
import os
import lgsvl
import math
import rospy
from geometry_msgs.msg import PoseStamped

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

#trigger_value=1→トリガが満たされた状態、trigger_value=2→トリガがまだ満たされていない状態、trigger_value=3→トリガが実行されたあとの状態
trigger_value = 2
#trigger_valueの値を変更済みかどうかの判断、True→変更済み、False→未変更
trigger_check = False

#test_positionの初期化
test_position = lgsvl.Vector(0, 0, 0) 

def worker1():
    global test_position

    sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)

    if sim.current_scene == "BorregasAve":
        sim.reset()
    else:
        sim.load("BorregasAve")
    spawns = sim.get_spawn()

# EGO
    state = lgsvl.AgentState()
    forward = lgsvl.utils.transform_to_forward(spawns[0])
    right = lgsvl.utils.transform_to_right(spawns[0])
    up = lgsvl.utils.transform_to_up(spawns[0])
    state.transform = spawns[0]
    a = sim.add_agent("Jaguar2015XE (Autoware)", lgsvl.AgentType.EGO, state)
    a.connect_bridge("localhost", 9090)

# NPC, 35 meters ahead, 20 meters right
    state = lgsvl.AgentState()
    state.transform.position = spawns[0].position + 35 * forward + -20 * right
    state.transform.rotation = lgsvl.Vector(0,180,0)
    npc = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)

# This block creates the list of waypoints that the NPC will follow
# Each waypoint consists of a position vector, speed, and an angular orientation vector
    waypoints = []
    test_waypoints = []

    layer_mask = 0
    layer_mask |= 1 << 0 # 0 is the layer for the road (default

    speed = 10
    angle = lgsvl.Vector(0,180,0)
    # Raycast the points onto the ground because BorregasAve is not flat
    hit = sim.raycast(spawns[0].position + 35 * forward + -20 * right, lgsvl.Vector(0,-1,0), layer_mask) 

    wp = lgsvl.DriveWaypoint(hit.point, speed, angle, 0, 0)
   
    test_position = hit.point

    waypoints.append(wp)

    # When the NPC is within 1m of the waypoint, this will be called
    def on_waypoint(agent, index):
        global trigger_value
        global test_position
        test_waypoints = []
        #トリガー用関数
        def trigger():
            #新たなwaypoint作成
            waypoints = []
            global trigger_value
            layer_mask = 0
            layer_mask |= 1 << 0 # 0 is the layer for the road (default)
            for i in range(40):
              speed = 10
              px = i
              py = 0
              pz = 0
              
              angle = lgsvl.Vector(0,180,0)

              # Raycast the points onto the ground because BorregasAve is not flat
              hit = sim.raycast(spawns[0].position + 35 * forward + -20 * right + px * right + pz * forward, lgsvl.Vector(0,-1,0), layer_mask) 
              wp2 = lgsvl.DriveWaypoint(hit.point, speed, angle, 0, 0)
              waypoints.append(wp2)

            npc.follow(waypoints)

            trigger_value = 3

        if trigger_value == 1:
            trigger()

        elif trigger_value == 2:
            test_position2 = lgsvl.DriveWaypoint(test_position, 10, lgsvl.Vector(0,180,0), 0,0)
            test_waypoints.append(test_position2)
            npc.on_waypoint_reached(on_waypoint)
            npc.follow(test_waypoints)
        else:
            pass

    def on_collision(agent1, agent2, contact):
        name1 = "STATIC OBSTACLE" if agent1 is None else agent1.name
        name2 = "STATIC OBSTACLE" if agent2 is None else agent2.name
        print("{} collided with {}".format(name1, name2))


    # The above function needs to be added to the list of callbacks for the NPC
    npc.on_waypoint_reached(on_waypoint)

    a.on_collision(on_collision)

    npc.follow(waypoints)

    input("Press Enter to run")

    sim.run(time_scale = 1.0)

def worker2():
    print("pepe")
    global trigger_value
    global trigger_check
    time.sleep(10)
    trigger_value = 1
    trigger_check = True

if __name__ == '__main__':
    #自車のposition値を受け取るノード
    # rospy.init_node('position_listener')
    
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)

    t1.start()
    t2.start()
