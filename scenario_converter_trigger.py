# -*- coding: utf-8 -*-

import sys
import make_curve
import numpy as np

Name = 0
ClassID = 1
Position = 2
Waypoint = 3
Waypoint_Num = 4
Speed = 5
Angle = 6
Trigger_check = 7
X = 0
Y = 1
Z = 2

def extract_non_ego_actors_line():
	# "filename" means the MATLAB file's name i.e. "test.m"

	filename = sys.argv
	# path = './input/' + filename[1]
	path = filename[1]

	non_ego_actors = []
	non_ego_actors_num = 0
	flag = 0

	# finding the string "non-ego actors" in the MATLAB file and appending the lines after the string to "non_ego_actors" variable
	with open(path, "r") as f:
		for line in f:
			if 'non-ego actors' in line:
				flag = 1
			if flag == 1:
				non_ego_actors.append(line)
	# the "non_ego_actors" variable includes the lines as follow
	# #  % Add the non-ego actors
	# # car1 = vehicle(scenario, ...
	# #     'ClassID', 1, ...
	# #     'Position', [37.8 49 0]);
	# # waypoints = [37.8 49 0;
	# #     35.5 24.2 0;
	# #     42.7 -6.4 0;
	# #     36.9 -40.5 0];
	# # speed = 30;
	# # trajectory(car1, waypoints, speed);
	# #
	# # pedestrian = actor(scenario, ...
	# #     'ClassID', 4, ...
	# #     'Length', 0.24, ...
	# #     'Width', 0.45, ...
	# #     'Height', 1.7, ...
	# #     'Position', [17.2 13.8 0], ...
	# #     'RCSPattern', [-8 -8;-8 -8]);
	# # waypoints = [17.2 13.8 0;
	# #     17.6 -6.7 0];
	# # speed = 1.5;
	# # trajectory(pedestrian, waypoints, speed);
	return non_ego_actors

def separate_each_actor(non_ego_actors):
	actor = []
	actor_array = []
	for line in non_ego_actors:
		if line == "\n":
			actor_array.append(actor)
			actor = []
		else:
			actor.append(line)
	return actor_array, len(actor_array)

def extract_class_id(line):
	class_id = int(line.split(",")[1])
	return class_id

def extract_coordinate(line):
	splited_blank = line.split()
	if "[" in line:
		if "]" in line:
			# "'Position', [37.8 49 0]);" -> splited_blank = ["[37.8", "49", "0]);"] -> xyz = [37.8, 49, 0]
			x = float(splited_blank[0][1:])
			y = float(splited_blank[1])
			z = float(splited_blank[2].split("]")[0])
		else:
			# "waypoints = [37.8 49 0;" -> splited_blank = ["waypoints [37.8", "49", "0;"] -> xyz = [37.8, 49, 0]
			x = float(splited_blank[0][1:])
			y = float(splited_blank[1])
			z = float(splited_blank[2][:-1])
	else:
		if "]" in line:
			x = float(splited_blank[0])
			y = float(splited_blank[1])
			z = float(splited_blank[2].split("]")[0])
		else:
			x = float(splited_blank[0])
			y = float(splited_blank[1])
			z = float(splited_blank[2][:-1])
	coordinate = [x, y, z]
	return coordinate

def extract_position(line):
	position = extract_coordinate(line.split(",")[1])
	return position

def separate_coordinate(waypoints):
	x = []
	y = []
	z = []
	for i in range(len(waypoints)):
		x.append(waypoints[i][X])
		y.append(waypoints[i][Y])
		z.append(waypoints[i][Z])
	separate_waypoints = [x, y, z]
	return separate_waypoints

def extract_waypoints(actor, start_index):
	waypoints_information = []
	waypoints = []
	index = start_index

	while "]" not in actor[index]:
		index = index + 1
	index = index + 1
	end_index = index

	for i in range(start_index, end_index):
		if i == start_index:
			waypoints.append(extract_coordinate(actor[i].split("=")[1]))
		else:
			waypoints.append(extract_coordinate(actor[i]))
	waypoints = (separate_coordinate(waypoints))

	return waypoints

def extract_speed(line):
	if "[" in line:
		speed = []
		split_equal = line.split("=")[1]
		split_semicolon = split_equal.split(";")
		for i in range(len(split_semicolon) - 1):
			if "[" in split_semicolon[i]:
				speed.append(float(split_semicolon[i][2:]))
			elif "]" in split_semicolon[i]:
				# for modify
				speed.append(float(split_semicolon[i][:-1]))
			else:
				speed.append(float(split_semicolon[i]))
	else:
		speed = float(line.split("=")[1][:-2])

	return speed
def extract_yaw(line):
	split_comma = line.split(",")[1]
	yaw = float(split_comma)
	return yaw

def add_position_to_waypoints(position):
	waypoints = []
	waypoints.append([position[0]])
	waypoints.append([position[1]])
	waypoints.append([position[2]])

	return waypoints

def extract_name(line):
	# line includes "'Name', 'trigger');"
	split_comma = line.split(",")[1]
	split_apostrophe = split_comma.split("'")
	name = split_apostrophe[1]
	return name

def extract_actor_information(actor_array, num):
	actor_information_array = []
	waypoints_array = []
	original_waypoints = []
	for i in range(num):
		actor_information = []
		count = 0
		flag_waypoints = False
		flag_speed = False
		flag_yaw = False
		for line in actor_array[i]:
			if "trajectory" not in line:
				if "ClassID" in line:
					class_id = extract_class_id(line)
				if "Position" in line:
					position = extract_position(line)
				if "waypoints" in line:
					waypoints = extract_waypoints(actor_array[i], count)
					flag_waypoints = True
				if "speed" in line:
					speed = extract_speed(line)
					flag_speed = True
				if "Yaw" in line:
					yaw = extract_yaw(line)
					# the positive direction is opposite
					yaw = -yaw
					flag_yaw = True
				if "Name" in line:
					name = extract_name(line)

			count = count + 1

		if flag_waypoints == False:
			waypoints = add_position_to_waypoints(position)
		if flag_speed == False:
			speed = 0.0
		if flag_yaw == False:
			yaw = False

		actor_information.append(name)
		actor_information.append(class_id)
		actor_information.append(position)
		actor_information.append(waypoints)
		actor_information.append(len(waypoints[X]))
		actor_information.append(speed)
		actor_information.append(yaw)
		actor_information.append(False) # for trigger check
		actor_information_array.append(actor_information)
		waypoints_array.append(waypoints)

	for i in range(len(waypoints_array)):
		original_waypoints.append(waypoints_array[i].copy())

	return actor_information_array, original_waypoints

def vehicle_curve(actor_information_array):
	for i in range(len(actor_information_array)):
		if actor_information_array[i][Waypoint_Num] > 2:
			if actor_information_array[i][ClassID] == 1:
				x, y = make_curve.make_curve2(actor_information_array[i][Waypoint][X], actor_information_array[i][Waypoint][Y])
				# actor_information_array[i][Waypoint][X].clear()
				# actor_information_array[i][Waypoint][Y].clear()
				# actor_information_array[i][Waypoint][Z].clear()
				x_array = []
				y_array = []
				z_array = []
				for j in range(100): # 100 waypoints
					# actor_information_array[i][Waypoint][X].append(x[j])
					# actor_information_array[i][Waypoint][Y].append(y[j])
					# actor_information_array[i][Waypoint][Z].append(0)
					x_array.append(x[j])
					y_array.append(y[j])
					z_array.append(0)
				actor_information_array[i][Waypoint][X] = x_array
				actor_information_array[i][Waypoint][Y] = y_array
				actor_information_array[i][Waypoint][Z] = z_array

				actor_information_array[i][Waypoint_Num] = 100

	return actor_information_array


def output_vehicle(waypoints, waypoints_num, speed, path, yaw, count_vehicle):
	init_pose = 'spawns[0].position + ' + str(waypoints[X][0]) + ' * forward + ' + str(waypoints[Y][0]) + ' * right'
	# print(waypoints_num)


	with open(path, mode = 'a') as f:
		f.write('state = lgsvl.AgentState()\n')
		f.write('layer_mask = 0\n')
		f.write('layer_mask |= 1 << 0\n')
		f.write('hit = sim.raycast(' + init_pose + ', lgsvl.Vector(0,-1,0), layer_mask)\n')
		f.write('state.transform.position = hit.point\n')

		if yaw == False:
			if waypoints_num > 1:
				pose = 'spawns[0].position + ' + str(waypoints[X][0]) + ' * forward + ' + str(waypoints[Y][0]) + ' * right'
				next_pose = 'spawns[0].position + ' + str(waypoints[X][1]) + ' * forward + ' + str(waypoints[Y][1])  +  ' * right'
				f.write('start = ' + pose + '\n')
				f.write('end = ' + next_pose + '\n')
				f.write('diff = end - start\n')
				f.write('angle = math.degrees(math.atan2(diff.x,diff.z)) \n')
				f.write('state.transform.rotation = lgsvl.Vector(0, angle, 0)\n')
			else:
				f.write('state.transform.rotation = spawns[0].rotation\n')

		else:
			f.write('state.transform.rotation = spawns[0].rotation + lgsvl.Vector(0,' + str(yaw) + ', 0)\n')
		f.write('npc' + str(count_vehicle) + ' = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)\n')
		f.write('waypoints' + str(count_vehicle) + ' = []\n')

		if waypoints_num == 1:
			pose = 'spawns[0].position + ' + str(waypoints[X][0]) + ' * forward + ' + str(waypoints[Y][0]) + ' * right'
			f.write('hit = sim.raycast(' + pose + ', lgsvl.Vector(0,-1,0), layer_mask)\n')
			f.write('waypoints' + str(count_vehicle) + '.append(lgsvl.DriveWaypoint(hit.point,  ' + str(speed[0]) + ', lgsvl.Vector(0, ' + str(yaw) + ', 0), 0))\n')
		else:
			for i in range(waypoints_num - 1):
				next_i = i + 1
				pose = 'spawns[0].position + ' + str(waypoints[X][i]) + ' * forward + ' + str(waypoints[Y][i]) + ' * right'
				next_pose = 'spawns[0].position + ' + str(waypoints[X][next_i]) + ' * forward + ' + str(waypoints[Y][next_i])  +  ' * right'
				f.write('start = ' + pose + '\n')
				f.write('end = ' + next_pose + '\n')
				f.write('diff = end - start\n')
				f.write('angle = math.degrees(math.atan2(diff.x,diff.z)) \n')
				f.write('hit = sim.raycast(' + pose + ', lgsvl.Vector(0,-1,0), layer_mask)\n')
				f.write('waypoints' + str(count_vehicle) + '.append(lgsvl.DriveWaypoint(hit.point, ' + str(speed[i]) + ', lgsvl.Vector(0, angle, 0), 0))\n')
			f.write('hit = sim.raycast(' + next_pose + ', lgsvl.Vector(0,-1,0), layer_mask)\n')
			f.write('waypoints' + str(count_vehicle) + '.append(lgsvl.DriveWaypoint(hit.point,  ' + str(speed[waypoints_num - 1]) + ', lgsvl.Vector(0, angle, 0), 0))\n')

		f.write('npc' + str(count_vehicle) + '.follow(waypoints' + str(count_vehicle) + ', loop=True)\n')
		f.write('\n\n')
	print("vehicle")


def output_pedestrian(waypoints, waypoints_num, path, count_pedestrian):
	Loop = False
	with open(path, mode = 'a') as f:
		f.write('wp' + str(count_pedestrian) + ' = []\n')
		for i in range(waypoints_num):
			f.write('wp' + str(count_pedestrian) + '.append(lgsvl.WalkWaypoint(spawns[0].position + ' + str(waypoints[X][i]) + ' * forward + ' + str(waypoints[Y][i]) + ' * right, 0))\n')
		f.write('state = lgsvl.AgentState()\n')
		f.write('state.transform = copy.deepcopy(spawns[0])\n')
		f.write('state.transform.position = wp' + str(count_pedestrian) + '[0].position\n')
		f.write('p' + str(count_pedestrian) + ' = sim.add_agent("Bob", lgsvl.AgentType.PEDESTRIAN, state)\n')
		if Loop == False:
			f.write('p' + str(count_pedestrian) + '.follow(wp' + str(count_pedestrian) + ', False)\n')
		else:
			if waypoints_num == 1:
				f.write('p' + str(count_pedestrian) + '.follow(wp' + str(count_pedestrian) + ', False)\n')
			else:
				f.write('p' + str(count_pedestrian) + '.follow(wp' + str(count_pedestrian) + ', True)\n')
		f.write('\n\n')


	print("pedestiran")

def make_path():
	filename = sys.argv
	filename[1] = filename[1][:-2]
	output_path = "./output/" + filename[1] + ".py"

	template_path = "./template.py"
	return output_path, template_path

def add_speed_parameter(speed, num):
	speed_array = []
	for i in range(num):
		speed_array.append(speed)
	return speed_array

def distance(point_from, point_to):
	distance = point_to - point_from
	return np.linalg.norm(distance)


def nearest_index(waypoint, original_waypoint):
	index = []
	count = 0
	pre_dis = 10**309
	for i in range(len(waypoint[X]) - 1):
		point_from = np.array([original_waypoint[X][count], original_waypoint[Y][count]])
		point_to = np.array([waypoint[X][i], waypoint[Y][i]])
		dis = distance(point_from, point_to)
		if pre_dis >= dis:
			pre_dis = dis
		else:
			index.append(i - 1)
			count += 1
			pre_dis = 10**309
	index.append(len(waypoint[X]) - 1)
	index.pop(0)

	return	index

def make_speed_list(speed, index):
	new_speed = []
	count = 0
	for i in range(len(index)):
		while count <= index[i]:
			new_speed.append(speed[i])
			count += 1
	return new_speed

def vehicle_speed(actor_information_array, original_waypoints):
	for i in range(len(actor_information_array)):
		if actor_information_array[i][ClassID] == 1:
			if type(actor_information_array[i][Speed]) == float:
				actor_information_array[i][Speed] = add_speed_parameter(actor_information_array[i][Speed], actor_information_array[i][Waypoint_Num])
			elif len(actor_information_array[i][Speed]) == 2:
				continue;
			else:
				index = nearest_index(actor_information_array[i][Waypoint], original_waypoints[i])
				actor_information_array[i][Speed] = make_speed_list(actor_information_array[i][Speed], index)
	return actor_information_array


def output_template_for_setting_simulator(template_path, output_path, start_or_end):
	if start_or_end == True:
		with open(output_path, mode = 'w'):
			pass

		with open(template_path, 'r') as f:
			with open(output_path, mode = 'a') as f2:
				for line in f:
					if "waypoint_checker" in line:
						break
					else:
						f2.write(line)
	elif start_or_end == False:
		flag = 0
		with open(template_path, 'r') as f:
			with open(output_path, mode = 'a') as f2:
				for line in f:
					if "waypoint_checked" in line:
						flag = 1
					elif flag == 1:
						f2.write(line)

def output_actor_information(actor_information_array, output_path):
	count_vehicle = 0
	count_pedestrian = 0
	for i in range(len(actor_information_array)):
		if actor_information_array[i][ClassID] == 1:
			output_vehicle(actor_information_array[i][Waypoint], actor_information_array[i][Waypoint_Num], actor_information_array[i][Speed], output_path, actor_information_array[i][Angle], count_vehicle)
			count_vehicle += 1
		elif actor_information_array[i][ClassID] == 4:
			output_pedestrian(actor_information_array[i][Waypoint], actor_information_array[i][Waypoint_Num], output_path, count_pedestrian)
			count_pedestrian += 1

def reverse_y_coordinate(actor_information_array):
	for i in range(len(actor_information_array)):
		for j in range(len(actor_information_array[i][Waypoint][Y])):
			actor_information_array[i][Waypoint][Y][j] = actor_information_array[i][Waypoint][Y][j] * -1
	return actor_information_array


def trigger_check(actor_information_array):
	for i in range(len(actor_information_array)):
		if actor_information_array[i][ClassID] == 1:
			for j in range(len(actor_information_array)):
				if actor_information_array[i][Name] == actor_information_array[j][Name] and actor_information_array[j][ClassID] == 6:
					actor_information_array[i][Trigger_check] = True

	return actor_information_array


def main():
	non_ego_actors = extract_non_ego_actors_line()
	actor_array, actors_num = separate_each_actor(non_ego_actors)
	actor_information_array, original_waypoints = extract_actor_information(actor_array, actors_num)
	actor_information_array = vehicle_curve(actor_information_array)
	actor_information_array = vehicle_speed(actor_information_array, original_waypoints)
	actor_information_array = reverse_y_coordinate(actor_information_array)
	actor_information_array = trigger_check(actor_information_array)
	print(actor_information_array)
	output_path, template_path = make_path()
	
	output_template_for_setting_simulator(template_path, output_path, True)
	output_actor_information(actor_information_array, output_path)
	output_template_for_setting_simulator(template_path, output_path, False)
	





if __name__ == '__main__':
	main()
