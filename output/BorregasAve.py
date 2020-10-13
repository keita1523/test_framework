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

while not a.bridge_connected:
  time.sleep(1)

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
state = lgsvl.AgentState()
layer_mask = 0
layer_mask |= 1 << 0
state.transform.position = spawns[0].position + 36.90000000000003 * forward + -50.100000000000016 * right
state.transform.rotation = lgsvl.Vector(0, 0, 0)
npc = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)
waypoints = []
start = spawns[0].position + 40.72834261907747 * forward + 39.67651641442642 * right
end = spawns[0].position + 36.90000000000003 * forward + -50.100000000000016 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.90000000000003 * forward + -50.100000000000016 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.90000000000003 * forward + -50.100000000000016 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.90000000000003 * forward + -50.100000000000016 * right
end = spawns[0].position + 37.39946212475289 * forward + -49.17446614261924 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.39946212475289 * forward + -49.17446614261924 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.39946212475289 * forward + -49.17446614261924 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.39946212475289 * forward + -49.17446614261924 * right
end = spawns[0].position + 37.87076617221507 * forward + -48.24984822782599 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.87076617221507 * forward + -48.24984822782599 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.87076617221507 * forward + -48.24984822782599 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.87076617221507 * forward + -48.24984822782599 * right
end = spawns[0].position + 38.31449216792199 * forward + -47.32612973079686 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.31449216792199 * forward + -47.32612973079686 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.31449216792199 * forward + -47.32612973079686 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.31449216792199 * forward + -47.32612973079686 * right
end = spawns[0].position + 38.73122013740907 * forward + -46.403294126708445 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.73122013740907 * forward + -46.403294126708445 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.73122013740907 * forward + -46.403294126708445 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.73122013740907 * forward + -46.403294126708445 * right
end = spawns[0].position + 39.121530106211736 * forward + -45.48132489073734 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.121530106211736 * forward + -45.48132489073734 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.121530106211736 * forward + -45.48132489073734 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.121530106211736 * forward + -45.48132489073734 * right
end = spawns[0].position + 39.48600209986542 * forward + -44.56020549806016 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.48600209986542 * forward + -44.56020549806016 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.48600209986542 * forward + -44.56020549806016 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.48600209986542 * forward + -44.56020549806016 * right
end = spawns[0].position + 39.82521614390553 * forward + -43.639919423853485 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.82521614390553 * forward + -43.639919423853485 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.82521614390553 * forward + -43.639919423853485 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.82521614390553 * forward + -43.639919423853485 * right
end = spawns[0].position + 40.13975226386749 * forward + -42.720450143293924 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.13975226386749 * forward + -42.720450143293924 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.13975226386749 * forward + -42.720450143293924 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.13975226386749 * forward + -42.720450143293924 * right
end = spawns[0].position + 40.430190485286744 * forward + -41.80178113155807 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.430190485286744 * forward + -41.80178113155807 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.430190485286744 * forward + -41.80178113155807 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.430190485286744 * forward + -41.80178113155807 * right
end = spawns[0].position + 40.697110833698694 * forward + -40.88389586382251 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.697110833698694 * forward + -40.88389586382251 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.697110833698694 * forward + -40.88389586382251 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.697110833698694 * forward + -40.88389586382251 * right
end = spawns[0].position + 40.941093334638786 * forward + -39.966777815263875 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.941093334638786 * forward + -39.966777815263875 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.941093334638786 * forward + -39.966777815263875 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.941093334638786 * forward + -39.966777815263875 * right
end = spawns[0].position + 41.16271801364242 * forward + -39.05041046105873 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.16271801364242 * forward + -39.05041046105873 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.16271801364242 * forward + -39.05041046105873 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.16271801364242 * forward + -39.05041046105873 * right
end = spawns[0].position + 41.36256489624503 * forward + -38.13477727638369 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.36256489624503 * forward + -38.13477727638369 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.36256489624503 * forward + -38.13477727638369 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.36256489624503 * forward + -38.13477727638369 * right
end = spawns[0].position + 41.54121400798203 * forward + -37.219861736415325 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.54121400798203 * forward + -37.219861736415325 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.54121400798203 * forward + -37.219861736415325 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.54121400798203 * forward + -37.219861736415325 * right
end = spawns[0].position + 41.699245374388866 * forward + -36.305647316330266 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.699245374388866 * forward + -36.305647316330266 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.699245374388866 * forward + -36.305647316330266 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.699245374388866 * forward + -36.305647316330266 * right
end = spawns[0].position + 41.83723902100093 * forward + -35.3921174913051 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.83723902100093 * forward + -35.3921174913051 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.83723902100093 * forward + -35.3921174913051 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.83723902100093 * forward + -35.3921174913051 * right
end = spawns[0].position + 41.95577497335367 * forward + -34.47925573651643 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.95577497335367 * forward + -34.47925573651643 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.95577497335367 * forward + -34.47925573651643 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.95577497335367 * forward + -34.47925573651643 * right
end = spawns[0].position + 42.055433256982525 * forward + -33.567045527140856 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.055433256982525 * forward + -33.567045527140856 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.055433256982525 * forward + -33.567045527140856 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.055433256982525 * forward + -33.567045527140856 * right
end = spawns[0].position + 42.13679389742287 * forward + -32.65547033835494 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.13679389742287 * forward + -32.65547033835494 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.13679389742287 * forward + -32.65547033835494 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.13679389742287 * forward + -32.65547033835494 * right
end = spawns[0].position + 42.200436920210166 * forward + -31.744513645335335 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.200436920210166 * forward + -31.744513645335335 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.200436920210166 * forward + -31.744513645335335 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.200436920210166 * forward + -31.744513645335335 * right
end = spawns[0].position + 42.24694235087981 * forward + -30.834158923258585 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.24694235087981 * forward + -30.834158923258585 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.24694235087981 * forward + -30.834158923258585 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.24694235087981 * forward + -30.834158923258585 * right
end = spawns[0].position + 42.27689021496726 * forward + -29.924389647301332 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.27689021496726 * forward + -29.924389647301332 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.27689021496726 * forward + -29.924389647301332 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.27689021496726 * forward + -29.924389647301332 * right
end = spawns[0].position + 42.29086053800791 * forward + -29.01518929264016 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.29086053800791 * forward + -29.01518929264016 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.29086053800791 * forward + -29.01518929264016 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.29086053800791 * forward + -29.01518929264016 * right
end = spawns[0].position + 42.289433345537205 * forward + -28.10654133445166 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.289433345537205 * forward + -28.10654133445166 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.289433345537205 * forward + -28.10654133445166 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.289433345537205 * forward + -28.10654133445166 * right
end = spawns[0].position + 42.273188663090565 * forward + -27.198429247912433 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.273188663090565 * forward + -27.198429247912433 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.273188663090565 * forward + -27.198429247912433 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.273188663090565 * forward + -27.198429247912433 * right
end = spawns[0].position + 42.24270651620339 * forward + -26.29083650819907 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.24270651620339 * forward + -26.29083650819907 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.24270651620339 * forward + -26.29083650819907 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.24270651620339 * forward + -26.29083650819907 * right
end = spawns[0].position + 42.19856693041112 * forward + -25.383746590488187 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.19856693041112 * forward + -25.383746590488187 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.19856693041112 * forward + -25.383746590488187 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.19856693041112 * forward + -25.383746590488187 * right
end = spawns[0].position + 42.14134993124919 * forward + -24.47714296995637 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.14134993124919 * forward + -24.47714296995637 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.14134993124919 * forward + -24.47714296995637 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.14134993124919 * forward + -24.47714296995637 * right
end = spawns[0].position + 42.071635544253 * forward + -23.571009121780214 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 42.071635544253 * forward + -23.571009121780214 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 42.071635544253 * forward + -23.571009121780214 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 42.071635544253 * forward + -23.571009121780214 * right
end = spawns[0].position + 41.99000379495799 * forward + -22.66532852113632 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.99000379495799 * forward + -22.66532852113632 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.99000379495799 * forward + -22.66532852113632 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.99000379495799 * forward + -22.66532852113632 * right
end = spawns[0].position + 41.8970347088996 * forward + -21.76008464320129 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.8970347088996 * forward + -21.76008464320129 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.8970347088996 * forward + -21.76008464320129 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.8970347088996 * forward + -21.76008464320129 * right
end = spawns[0].position + 41.7933083116132 * forward + -20.855260963151714 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.7933083116132 * forward + -20.855260963151714 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.7933083116132 * forward + -20.855260963151714 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.7933083116132 * forward + -20.855260963151714 * right
end = spawns[0].position + 41.679404628634266 * forward + -19.9508409561642 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.679404628634266 * forward + -19.9508409561642 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.679404628634266 * forward + -19.9508409561642 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.679404628634266 * forward + -19.9508409561642 * right
end = spawns[0].position + 41.5559036854982 * forward + -19.046808097415337 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.5559036854982 * forward + -19.046808097415337 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.5559036854982 * forward + -19.046808097415337 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.5559036854982 * forward + -19.046808097415337 * right
end = spawns[0].position + 41.42338550774043 * forward + -18.143145862081724 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.42338550774043 * forward + -18.143145862081724 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.42338550774043 * forward + -18.143145862081724 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.42338550774043 * forward + -18.143145862081724 * right
end = spawns[0].position + 41.28243012089638 * forward + -17.239837725339964 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.28243012089638 * forward + -17.239837725339964 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.28243012089638 * forward + -17.239837725339964 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.28243012089638 * forward + -17.239837725339964 * right
end = spawns[0].position + 41.13361755050146 * forward + -16.336867162366648 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 41.13361755050146 * forward + -16.336867162366648 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 41.13361755050146 * forward + -16.336867162366648 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 41.13361755050146 * forward + -16.336867162366648 * right
end = spawns[0].position + 40.977527822091105 * forward + -15.434217648338382 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.977527822091105 * forward + -15.434217648338382 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.977527822091105 * forward + -15.434217648338382 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.977527822091105 * forward + -15.434217648338382 * right
end = spawns[0].position + 40.81474096120075 * forward + -14.531872658431762 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.81474096120075 * forward + -14.531872658431762 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.81474096120075 * forward + -14.531872658431762 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.81474096120075 * forward + -14.531872658431762 * right
end = spawns[0].position + 40.645836993365805 * forward + -13.629815667823385 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.645836993365805 * forward + -13.629815667823385 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.645836993365805 * forward + -13.629815667823385 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.645836993365805 * forward + -13.629815667823385 * right
end = spawns[0].position + 40.47139594412168 * forward + -12.728030151689826 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.47139594412168 * forward + -12.728030151689826 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.47139594412168 * forward + -12.728030151689826 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.47139594412168 * forward + -12.728030151689826 * right
end = spawns[0].position + 40.29199783900383 * forward + -11.826499585207724 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.29199783900383 * forward + -11.826499585207724 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.29199783900383 * forward + -11.826499585207724 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.29199783900383 * forward + -11.826499585207724 * right
end = spawns[0].position + 40.10822270354765 * forward + -10.925207443553653 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.10822270354765 * forward + -10.925207443553653 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.10822270354765 * forward + -10.925207443553653 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.10822270354765 * forward + -10.925207443553653 * right
end = spawns[0].position + 39.92065056328858 * forward + -10.024137201904216 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.92065056328858 * forward + -10.024137201904216 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.92065056328858 * forward + -10.024137201904216 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.92065056328858 * forward + -10.024137201904216 * right
end = spawns[0].position + 39.72986144376204 * forward + -9.123272335436006 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.72986144376204 * forward + -9.123272335436006 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.72986144376204 * forward + -9.123272335436006 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.72986144376204 * forward + -9.123272335436006 * right
end = spawns[0].position + 39.53643537050346 * forward + -8.222596319325628 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.53643537050346 * forward + -8.222596319325628 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.53643537050346 * forward + -8.222596319325628 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.53643537050346 * forward + -8.222596319325628 * right
end = spawns[0].position + 39.34095236904825 * forward + -7.322092628749677 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.34095236904825 * forward + -7.322092628749677 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.34095236904825 * forward + -7.322092628749677 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.34095236904825 * forward + -7.322092628749677 * right
end = spawns[0].position + 39.14399246493185 * forward + -6.421744738884748 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.14399246493185 * forward + -6.421744738884748 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.14399246493185 * forward + -6.421744738884748 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.14399246493185 * forward + -6.421744738884748 * right
end = spawns[0].position + 38.94613568368966 * forward + -5.521536124907446 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.94613568368966 * forward + -5.521536124907446 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.94613568368966 * forward + -5.521536124907446 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.94613568368966 * forward + -5.521536124907446 * right
end = spawns[0].position + 38.74796205085713 * forward + -4.621450261994362 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.74796205085713 * forward + -4.621450261994362 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.74796205085713 * forward + -4.621450261994362 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.74796205085713 * forward + -4.621450261994362 * right
end = spawns[0].position + 38.55005159196968 * forward + -3.7214706253220946 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.55005159196968 * forward + -3.7214706253220946 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.55005159196968 * forward + -3.7214706253220946 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.55005159196968 * forward + -3.7214706253220946 * right
end = spawns[0].position + 38.352984332562706 * forward + -2.821580690067244 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.352984332562706 * forward + -2.821580690067244 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.352984332562706 * forward + -2.821580690067244 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.352984332562706 * forward + -2.821580690067244 * right
end = spawns[0].position + 38.15734029817166 * forward + -1.921763931406404 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.15734029817166 * forward + -1.921763931406404 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.15734029817166 * forward + -1.921763931406404 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.15734029817166 * forward + -1.921763931406404 * right
end = spawns[0].position + 37.96369951433195 * forward + -1.0220038245161795 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.96369951433195 * forward + -1.0220038245161795 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.96369951433195 * forward + -1.0220038245161795 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.96369951433195 * forward + -1.0220038245161795 * right
end = spawns[0].position + 37.77264200657901 * forward + -0.12228384457316555 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.77264200657901 * forward + -0.12228384457316555 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.77264200657901 * forward + -0.12228384457316555 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.77264200657901 * forward + -0.12228384457316555 * right
end = spawns[0].position + 37.584747800448255 * forward + 0.777412533246042 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.584747800448255 * forward + 0.777412533246042 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.584747800448255 * forward + 0.777412533246042 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.584747800448255 * forward + 0.777412533246042 * right
end = spawns[0].position + 37.40059692147511 * forward + 1.677101833764846 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.40059692147511 * forward + 1.677101833764846 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.40059692147511 * forward + 1.677101833764846 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.40059692147511 * forward + 1.677101833764846 * right
end = spawns[0].position + 37.22076939519501 * forward + 2.576800581806645 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.22076939519501 * forward + 2.576800581806645 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.22076939519501 * forward + 2.576800581806645 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.22076939519501 * forward + 2.576800581806645 * right
end = spawns[0].position + 37.04584524714337 * forward + 3.4765253021948466 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.04584524714337 * forward + 3.4765253021948466 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.04584524714337 * forward + 3.4765253021948466 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.04584524714337 * forward + 3.4765253021948466 * right
end = spawns[0].position + 36.87640450285561 * forward + 4.3762925197528455 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.87640450285561 * forward + 4.3762925197528455 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.87640450285561 * forward + 4.3762925197528455 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.87640450285561 * forward + 4.3762925197528455 * right
end = spawns[0].position + 36.713027187867155 * forward + 5.276118759304051 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.713027187867155 * forward + 5.276118759304051 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.713027187867155 * forward + 5.276118759304051 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.713027187867155 * forward + 5.276118759304051 * right
end = spawns[0].position + 36.55629332771343 * forward + 6.17602054567186 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.55629332771343 * forward + 6.17602054567186 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.55629332771343 * forward + 6.17602054567186 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.55629332771343 * forward + 6.17602054567186 * right
end = spawns[0].position + 36.40678294792987 * forward + 7.0760144036796735 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.40678294792987 * forward + 7.0760144036796735 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.40678294792987 * forward + 7.0760144036796735 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.40678294792987 * forward + 7.0760144036796735 * right
end = spawns[0].position + 36.265076074051876 * forward + 7.9761168581509 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.265076074051876 * forward + 7.9761168581509 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.265076074051876 * forward + 7.9761168581509 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.265076074051876 * forward + 7.9761168581509 * right
end = spawns[0].position + 36.13175273161489 * forward + 8.876344433908937 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.13175273161489 * forward + 8.876344433908937 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.13175273161489 * forward + 8.876344433908937 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.13175273161489 * forward + 8.876344433908937 * right
end = spawns[0].position + 36.00739294615432 * forward + 9.776713655777186 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.00739294615432 * forward + 9.776713655777186 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.00739294615432 * forward + 9.776713655777186 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.00739294615432 * forward + 9.776713655777186 * right
end = spawns[0].position + 35.89257674320561 * forward + 10.677241048579056 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.89257674320561 * forward + 10.677241048579056 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.89257674320561 * forward + 10.677241048579056 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.89257674320561 * forward + 10.677241048579056 * right
end = spawns[0].position + 35.78788414830416 * forward + 11.577943137137943 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.78788414830416 * forward + 11.577943137137943 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.78788414830416 * forward + 11.577943137137943 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.78788414830416 * forward + 11.577943137137943 * right
end = spawns[0].position + 35.693895186985415 * forward + 12.47883644627725 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.693895186985415 * forward + 12.47883644627725 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.693895186985415 * forward + 12.47883644627725 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.693895186985415 * forward + 12.47883644627725 * right
end = spawns[0].position + 35.61118988478479 * forward + 13.379937500820375 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.61118988478479 * forward + 13.379937500820375 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.61118988478479 * forward + 13.379937500820375 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.61118988478479 * forward + 13.379937500820375 * right
end = spawns[0].position + 35.540348267237704 * forward + 14.28126282559073 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.540348267237704 * forward + 14.28126282559073 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.540348267237704 * forward + 14.28126282559073 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.540348267237704 * forward + 14.28126282559073 * right
end = spawns[0].position + 35.481950359879576 * forward + 15.182828945411709 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.481950359879576 * forward + 15.182828945411709 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.481950359879576 * forward + 15.182828945411709 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.481950359879576 * forward + 15.182828945411709 * right
end = spawns[0].position + 35.43657618824585 * forward + 16.08465238510672 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.43657618824585 * forward + 16.08465238510672 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.43657618824585 * forward + 16.08465238510672 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.43657618824585 * forward + 16.08465238510672 * right
end = spawns[0].position + 35.404805777871935 * forward + 16.986749669499154 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.404805777871935 * forward + 16.986749669499154 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.404805777871935 * forward + 16.986749669499154 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.404805777871935 * forward + 16.986749669499154 * right
end = spawns[0].position + 35.38721915429326 * forward + 17.88913732341243 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.38721915429326 * forward + 17.88913732341243 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.38721915429326 * forward + 17.88913732341243 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.38721915429326 * forward + 17.88913732341243 * right
end = spawns[0].position + 35.38439634304524 * forward + 18.791831871669935 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.38439634304524 * forward + 18.791831871669935 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.38439634304524 * forward + 18.791831871669935 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.38439634304524 * forward + 18.791831871669935 * right
end = spawns[0].position + 35.396917369663306 * forward + 19.694849839095077 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.396917369663306 * forward + 19.694849839095077 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.396917369663306 * forward + 19.694849839095077 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.396917369663306 * forward + 19.694849839095077 * right
end = spawns[0].position + 35.425362259682885 * forward + 20.598207750511268 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.425362259682885 * forward + 20.598207750511268 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.425362259682885 * forward + 20.598207750511268 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.425362259682885 * forward + 20.598207750511268 * right
end = spawns[0].position + 35.470311038639394 * forward + 21.501922130741892 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.470311038639394 * forward + 21.501922130741892 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.470311038639394 * forward + 21.501922130741892 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.470311038639394 * forward + 21.501922130741892 * right
end = spawns[0].position + 35.532343732068256 * forward + 22.40600950461036 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.532343732068256 * forward + 22.40600950461036 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.532343732068256 * forward + 22.40600950461036 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.532343732068256 * forward + 22.40600950461036 * right
end = spawns[0].position + 35.612040365504896 * forward + 23.310486396940085 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.612040365504896 * forward + 23.310486396940085 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.612040365504896 * forward + 23.310486396940085 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.612040365504896 * forward + 23.310486396940085 * right
end = spawns[0].position + 35.70998096448474 * forward + 24.215369332554452 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.70998096448474 * forward + 24.215369332554452 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.70998096448474 * forward + 24.215369332554452 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.70998096448474 * forward + 24.215369332554452 * right
end = spawns[0].position + 35.82674555454321 * forward + 25.120674836276866 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.82674555454321 * forward + 25.120674836276866 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.82674555454321 * forward + 25.120674836276866 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.82674555454321 * forward + 25.120674836276866 * right
end = spawns[0].position + 35.96291416121572 * forward + 26.026419432930727 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 35.96291416121572 * forward + 26.026419432930727 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 35.96291416121572 * forward + 26.026419432930727 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 35.96291416121572 * forward + 26.026419432930727 * right
end = spawns[0].position + 36.119066810037715 * forward + 26.93261964733945 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.119066810037715 * forward + 26.93261964733945 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.119066810037715 * forward + 26.93261964733945 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.119066810037715 * forward + 26.93261964733945 * right
end = spawns[0].position + 36.295783526544604 * forward + 27.839292004326424 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.295783526544604 * forward + 27.839292004326424 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.295783526544604 * forward + 27.839292004326424 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.295783526544604 * forward + 27.839292004326424 * right
end = spawns[0].position + 36.493644336271814 * forward + 28.74645302871506 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.493644336271814 * forward + 28.74645302871506 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.493644336271814 * forward + 28.74645302871506 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.493644336271814 * forward + 28.74645302871506 * right
end = spawns[0].position + 36.713229264754766 * forward + 29.654119245328758 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.713229264754766 * forward + 29.654119245328758 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.713229264754766 * forward + 29.654119245328758 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.713229264754766 * forward + 29.654119245328758 * right
end = spawns[0].position + 36.95511833752889 * forward + 30.562307178990913 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 36.95511833752889 * forward + 30.562307178990913 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 36.95511833752889 * forward + 30.562307178990913 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 36.95511833752889 * forward + 30.562307178990913 * right
end = spawns[0].position + 37.2198915801296 * forward + 31.471033354524938 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.2198915801296 * forward + 31.471033354524938 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.2198915801296 * forward + 31.471033354524938 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.2198915801296 * forward + 31.471033354524938 * right
end = spawns[0].position + 37.50812901809232 * forward + 32.38031429675423 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.50812901809232 * forward + 32.38031429675423 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.50812901809232 * forward + 32.38031429675423 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.50812901809232 * forward + 32.38031429675423 * right
end = spawns[0].position + 37.820410676952484 * forward + 33.290166530502184 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 37.820410676952484 * forward + 33.290166530502184 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 37.820410676952484 * forward + 33.290166530502184 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 37.820410676952484 * forward + 33.290166530502184 * right
end = spawns[0].position + 38.15731658224551 * forward + 34.200606580592215 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.15731658224551 * forward + 34.200606580592215 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.15731658224551 * forward + 34.200606580592215 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.15731658224551 * forward + 34.200606580592215 * right
end = spawns[0].position + 38.51942675950682 * forward + 35.111650971847716 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.51942675950682 * forward + 35.111650971847716 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.51942675950682 * forward + 35.111650971847716 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.51942675950682 * forward + 35.111650971847716 * right
end = spawns[0].position + 38.90732123427183 * forward + 36.0233162290921 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 38.90732123427183 * forward + 36.0233162290921 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 38.90732123427183 * forward + 36.0233162290921 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 38.90732123427183 * forward + 36.0233162290921 * right
end = spawns[0].position + 39.32158003207599 * forward + 36.93561887714876 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.32158003207599 * forward + 36.93561887714876 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.32158003207599 * forward + 36.93561887714876 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.32158003207599 * forward + 36.93561887714876 * right
end = spawns[0].position + 39.7627831784547 * forward + 37.8485754408411 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 39.7627831784547 * forward + 37.8485754408411 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 39.7627831784547 * forward + 37.8485754408411 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 39.7627831784547 * forward + 37.8485754408411 * right
end = spawns[0].position + 40.23151069894338 * forward + 38.76220244499251 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.23151069894338 * forward + 38.76220244499251 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.23151069894338 * forward + 38.76220244499251 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
start = spawns[0].position + 40.23151069894338 * forward + 38.76220244499251 * right
end = spawns[0].position + 40.72834261907747 * forward + 39.67651641442642 * right
diff = end - start
angle = math.degrees(math.atan2(diff.x,diff.z)) 
hit = sim.raycast(spawns[0].position + 40.72834261907747 * forward + 39.67651641442642 * right, lgsvl.Vector(0,-1,0), layer_mask)
waypoints.append(lgsvl.DriveWaypoint(spawns[0].position + 40.72834261907747 * forward + 39.67651641442642 * right + up * hit.point + 1.08,  30.0, lgsvl.Vector(0, angle, 0), 0)),
npc.follow(waypoints, loop=True)
print("")
Pedestrian1 = []
Pedestrian1.append(lgsvl.WalkWaypoint(spawns[0].position + 21.11 * forward + -13.47 * right, 0))
Pedestrian1.append(lgsvl.WalkWaypoint(spawns[0].position + 21.3 * forward + 6.75 * right, 0))
state = lgsvl.AgentState()
state.transform.position = spawns[0].position + 21.11 * forward + -13.47 * right
state.transform.rotation = spawns[0].rotation
name = random.choice(names)
p = sim.add_agent(name, lgsvl.AgentType.PEDESTRIAN, state)
p.follow(Pedestrian1, False)
#waypoint_checked

input("Press Enter to start")

sim.run()
