#!/usr/bin/env python3
#
# Autoware test
# Ego agent + many pedestrians
# reference : Quick Start sample No.17 and No.22 . 
#

import os
import lgsvl
import random
import time
import math
import cmath
import copy

sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)
if sim.current_scene == "BorregasAve":
  sim.reset()

else:
	sim.load("BorregasAve")

spawns = sim.get_spawn()

state = lgsvl.AgentState()
state.transform = spawns[0]

a = sim.add_agent("Jaguar2015XE (Autoware)", lgsvl.AgentType.EGO, state)

print("Bridge connected:", a.bridge_connected)

a.connect_bridge("localhost", 9090)

print("Waiting for connection...")

# while not a.bridge_connected:
#   time.sleep(1)

print("Bridge connected:", a.bridge_connected)

#######
forward = lgsvl.utils.transform_to_forward(spawns[0])
right = lgsvl.utils.transform_to_right(spawns[0])
up = lgsvl.utils.transform_to_up(spawns[0])


sx = state.transform.position.x
sy = state.transform.position.y
sz = state.transform.position.z

names = ["Bob", "EntrepreneurFemale", "Howard", "Johny", "Pamela", "Presley", "Robin", "Stephen", "Zoe"]

#waypoint_checker

print(spawns[0])

# for i in range(20*6):
for i in range(6):
  start = spawns[0].position + (5 + (1.0 * (i//6))) * forward - (2 + (1.0 * (i % 6))) * right
  end = start + 10 * forward

# Give waypoints for the spawn location and 10m ahead
  wp = [ lgsvl.WalkWaypoint(start, 0),
         lgsvl.WalkWaypoint(end, 0),
       ]

  state = lgsvl.AgentState()
  state.transform.position = start
  state.transform.rotation = spawns[0].rotation
  name = random.choice(names)


  p = sim.add_agent(name, lgsvl.AgentType.PEDESTRIAN, state)
  p.follow(wp, True)

state = lgsvl.AgentState()
state.transform.position = lgsvl.Vector(-20, -1.8, 30)  # 位置 Vector(左方向＋, 上方向＋, 後方＋)
state.transform.rotation = lgsvl.Vector(0, 0, 0)
npc1 = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)
waypoints = [
  lgsvl.DriveWaypoint(lgsvl.Vector(-30, -2, -5), 5, lgsvl.Vector(0, 194, 0), 0, False, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(-20, -2, -20), 10, lgsvl.Vector(0, 150, 0), 0, False, 0),
  lgsvl.DriveWaypoint(lgsvl.Vector(-10, -2, 0), 20, lgsvl.Vector(0, 40, 0), 0),   # 引数省略
  lgsvl.DriveWaypoint(lgsvl.Vector(-3, -1.8, 30), 30, lgsvl.Vector(0, 14, 0), 0),    # 引数省略
  lgsvl.DriveWaypoint(lgsvl.Vector(-20, -1.8, 20), 40, lgsvl.Vector(0, 280, 0), 0, False, 0),
]

npc1.follow(waypoints, loop=True)


#waypoint_checked

input("Press Enter to start")

sim.run()
