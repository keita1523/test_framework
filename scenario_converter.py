# -*- coding: utf-8 -*-

import sys
import make_curve




# "filename" means the MATLAB file's name i.e. "test.m"
filename = sys.argv

path = './' + filename[1]

flag = 0
non_ego_actors = []
non_ego_actors_num = 0

# finding the string "non-ego actors" in the MATLAB file and appending the lines after the string to "non_ego_actors" variable
with open(path, "r") as f:
	for line in f:
		if 'non-ego actors' in line:
			flag = 1
		if flag == 1:
			non_ego_actors.append(line)

# the "non_ego_actors" variable includes the lines as follow
# % Add the non-ego actors
# car1 = vehicle(scenario, ...
#     'ClassID', 1, ...
#     'Position', [37.8 49 0]);
# waypoints = [37.8 49 0;
#     35.5 24.2 0;
#     42.7 -6.4 0;
#     36.9 -40.5 0];
# speed = 30;
# trajectory(car1, waypoints, speed);

# pedestrian = actor(scenario, ...
#     'ClassID', 4, ...
#     'Length', 0.24, ...
#     'Width', 0.45, ...
#     'Height', 1.7, ...
#     'Position', [17.2 13.8 0], ...
#     'RCSPattern', [-8 -8;-8 -8]);
# waypoints = [17.2 13.8 0;
#     17.6 -6.7 0];
# speed = 1.5;
# trajectory(pedestrian, waypoints, speed);


def extract_actor_information(actors_information):

	Position = [[],[],[]]
	delete_brackets = [[],[],[]]
	waypoints_flag = 0
	waypoints_counter = 0
	count = 0
	waypoints = [[],[],[]]
	waypoints_array = [[],[],[]]
	waypoints_info = []
	speed = []
	delete_semicolon = []
	speed_count = 0

	for line in actors_information:
		# "trajectory" is the sign for the end of the required information
		if 'trajectory' in line:
			waypoints_flag = 0
			continue
		else:
			if 'ClassID' in line:
				# extracting the number X from the string of 
				# "'ClassID', X, ..." as type of "int"
				waypoints_flag = 0
				splited_comma = line.split(',')
				ClassID = int(splited_comma[1])

			if 'Position' in line:
				# extracting the coordinates from the string of
				# "'Position', [37.8 49 0]);" as type of "float"
				waypoints_flag = 0
				splited_comma = line.split(',')
				splited_blank = splited_comma[1].split()

				delete_brackets[0] = splited_blank[0][1:]
				delete_brackets[1] = splited_blank[1]
				delete_brackets[2] = splited_blank[2].split(']')[0]

				for i in range(3):
					Position[i] = float(delete_brackets[i])

			if 'speed' in line:
				# "speed" parameter is one value, 30 by default
				# but, if user changes the speed, the parameter will be one array.
				# extracting the speed from the string of 
				# "speed = 30;" or "speed = [30;30;15;30];" 
				waypoints_flag = 0

				splited_equal = line.split('=')
				delete_semicolon = splited_equal[1].split(';')
				speed_count = splited_equal[1].count(';')
				if speed_count  == 1:
					speed.append(float(delete_semicolon[0]))
				else:
					for i in range(speed_count):
						if i == 0:
							speed.append(float(delete_semicolon[i][2:]))
						elif i == speed_count-1:
							speed.append(float(delete_semicolon[i][:-1]))
						else:
							speed.append(float(delete_semicolon[i]))
				


			if 'waypoints =' in line:
				# extracting the wayponts and the number of the waypoints from the lines as follow
				## waypoints = [18.4 -2.8 0;
			    ## 36 -0.7 0;
    			## 41.1 -11.8 0;
			    ## 18.3 -27.8 0;
			    ## 8.3 -23.8 0;
			    ## 6 -7 0;
			    ## 6.7 16.1 0];

			    # separating the string, "waypoints =" and the coordinates at the first line
				waypoints_flag = 1
				waypoints_counter = waypoints_counter + 1
				splited_equal = line.split('=')
				waypoints_info.append(splited_equal[1])

			elif waypoints_flag == 1:
				# the other lines are appended by there
				waypoints_info.append(line)
				waypoints_counter = waypoints_counter + 1
	# extracting the coordinates of the waypoints
	for line in waypoints_info:
		# the first line and end line include "[" and "];", respectively.
		if count == 0:
			line = line[2:]
		if count == waypoints_counter-1:
			line = line[:-2]

		count = count + 1
		splited_blank = line.split()
		waypoints_array[0] = splited_blank[0]
		waypoints_array[1] = splited_blank[1]
		waypoints_array[2] = splited_blank[2][:-1]

		waypoints[0].append(float(waypoints_array[0]))
		waypoints[1].append(float(waypoints_array[1]))
		waypoints[2].append(float(waypoints_array[2]))


	return ClassID, Position, waypoints, waypoints_counter, speed


def pedestrian_actors(pedestrian,waypoints, waypoints_num):
	for i in range(waypoints_num):
		with open(path, mode = 'a') as f:
			pedestrian_append = pedestrian + '.append(lgsvl.WalkWaypoint(spawns[0].position + ' + str(waypoints[0][i]) + ' * forward + ' + str(waypoints[1][i]) + ' * right, 0))'
			f.write(pedestrian_append + '\n')
		if i == 0:
			init_pose = 'spawns[0].position + ' + str(waypoints[0][i]) + ' * forward + ' + str(waypoints[1][i]) + ' * right'
	with open(path, mode = 'a') as f:
		f.write('state = lgsvl.AgentState()\n')
		f.write('state.transform.position = ' + init_pose + '\n')
		f.write('state.transform.rotation = spawns[0].rotation\n')
		f.write('name = random.choice(names)\n')
		f.write('p = sim.add_agent(name, lgsvl.AgentType.PEDESTRIAN, state)\n')
		f.write('p.follow(' + pedestrian + ', False)\n')

def vehicle_actors(waypoints, waypoints_num, speed):
	init_pose = 'spawns[0].position + ' + str(waypoints[0][0]) + ' * forward + ' + str(waypoints[1][0]) + ' * right'


	with open(path, mode = 'a') as f:
		f.write('state = lgsvl.AgentState()\n')
		f.write('layer_mask = 0\n')
		f.write('layer_mask |= 1 << 0\n')
		f.write('state.transform.position = ' + init_pose + '\n')
		f.write('state.transform.rotation = lgsvl.Vector(0, 0, 0)\n')
		f.write('npc = sim.add_agent("Sedan", lgsvl.AgentType.NPC, state)\n')
		f.write('waypoints = []\n')
		for i in range(waypoints_num):
			index = (waypoints_num + i - 1) % waypoints_num
			pose = 'spawns[0].position + ' + str(waypoints[0][i]) + ' * forward + ' + str(waypoints[1][i]) + ' * right'
			pre_pose = 'spawns[0].position + ' + str(waypoints[0][index]) + ' * forward + ' + str(waypoints[1][index])  +  ' * right'
			f.write('start = ' + pre_pose + '\n')
			f.write('end = ' + pose + '\n')
			f.write('diff = end - start\n')
			f.write('angle = math.degrees(math.atan2(diff.x,diff.z)) \n')
			# f.write('if angle > 0 : angle = angle - 180 \n')
			f.write('hit = sim.raycast(' + pose + ', lgsvl.Vector(0,-1,0), layer_mask)\n')
			# pose = '(' + str(waypoints[0][i]) + ', ' + str(waypoints[1][i]) + ', ' + str(waypoints[2][i]) + ')'
			f.write('waypoints.append(lgsvl.DriveWaypoint(' + pose + ' + up * hit.point + 1.08,  ' + str(speed[i]) + ', lgsvl.Vector(0, angle, 0), 0)),\n')
			# f.write('waypoints.append(lgsvl.DriveWaypoint(' + pose + ', ' + str(speed[i]) + ', lgsvl.Vector(0, 0, 0), 0)),\n')
			# f.write('print("hit.point, up = ", hit.point, up)\n')
			# f.write('print("waypoint = ",' + pose + ' + up * hit.point)\n')
		f.write('npc.follow(waypoints, loop=True)\n')
		f.write('print("")\n')
	


def judge_ClassID():

	for i in range(non_ego_actors_num):
		if extracted_information[i][0] == 4:
			pedestrian = 'Pedestrian'
			pedestrian = pedestrian + str(i)
			with open(path, mode = 'a') as f:
				f.write(pedestrian + ' = []\n')
			pedestrian_actors(pedestrian, extracted_information[i][2], extracted_information[i][3])

		if extracted_information[i][0] == 1 or extracted_information[i][0] == 2:
			x = []
			y = []
			clothoid_waypoints = [[],[]]
			clothoid_speed = []
			if extracted_information[i][3] > 2:
				x, y = make_curve.make_curve2(extracted_information[i][2][0], extracted_information[i][2][1])
				step = 10
				print(x,y)
				waypoints_num = len(x)

				# waypoints_num = int(waypoints_num/step)
				for j in range(waypoints_num):
					if j % step == 0:
						clothoid_waypoints[0].append(x[j])
						clothoid_waypoints[1].append(y[j])

				waypoints_num = len(clothoid_waypoints[0])
				speed_flag = 0
				if len(extracted_information[i][4]) >= 2: speed_flag = 1

				count = 0
				for j in range(waypoints_num):
					
					if speed_flag == 0:
						clothoid_speed.append(extracted_information[i][4][0])
					else:
												
						if j % 10 == 9:
							clothoid_speed.append(extracted_information[i][4][count])
							count = count + 1

						else:
							clothoid_speed.append(extracted_information[i][4][count])


			else:
				clothoid_waypoints = extracted_information[i][2]
				waypoints_num = extracted_information[i][3]
				clothoid_speed = extracted_information[i][4]


			# print(x, y)
			# print(len(clothoid_waypoints))
			# print(len(x))
			# print(len(y))



			# vehicle_actors(extracted_information[i][2], extracted_information[i][3], extracted_information[i][4])
			vehicle_actors(clothoid_waypoints, waypoints_num, clothoid_speed)



# "actors_information" variable includes as folow lines

## 'ClassID', 1, ...
##     'Position', [37.8 49 0]);
## waypoints = [37.8 49 0;
##     35.5 24.2 0;
##     42.7 -6.4 0;
##     36.9 -40.5 0];
## speed = 30;
## trajectory(car1, waypoints, speed);
##
## pedestrian = actor(scenario, ...

# and "extracted_information" variable extracts the information of 
# the ClassID, Position, waypoints, the number of waypoints, and speed
# from the "actors_information" variable.

X = 0
Y = 1
Z = 2
CLASSID = 0

actors_information = []
extracted_information = []

flag = 0
for line in non_ego_actors:
	if 'ClassID' in line and flag == 1:
		extracted_information.append(extract_actor_information(actors_information))
		actors_information.clear()
		actors_information.append(line)
		flag = 0

	if 'ClassID' in line:
		flag = 1
		non_ego_actors_num = non_ego_actors_num + 1
	if flag == 1:
		actors_information.append(line)
extracted_information.append(extract_actor_information(actors_information))


for i in range(non_ego_actors_num):
	if extracted_information[i][3] == 0:
		extracted_information[i][2][0].append(extracted_information[i][1][0])
		extracted_information[i][2][1].append(extracted_information[i][1][1])
		extracted_information[i][2][2].append(extracted_information[i][1][2])


		l = list(extracted_information[i])
		l[3] = 1
		l[4] = [0]
		extracted_information[i] = tuple(l)



# convert Y coordinate
for i in range(non_ego_actors_num):
	for j in range(extracted_information[i][3]):
		extracted_information[i][2][1][j] = extracted_information[i][2][1][j] * -1




# output actors information other file
filename[1] = filename[1][:-2]
path = './output/' + filename[1] + '.py'






#次はここから　乗用車を表示できるようにする経路については後で考える

# copying the essential settings from the template.py
path_sample = './template.py'
sample_line = []
flag = 0

with open(path, mode = 'w'):
	pass


with open(path_sample, "r") as f:
	for line in f:
		if 'waypoint_checked' in line:
			flag = 0

		if flag == 0:
			with open(path, mode = 'a') as f2:
				f2.write(line)

		if 'waypoint_checker' in line:
			flag = 1
			# with open(path, mode = 'a') as f2:
			# 	f2.write('wp = []\n')
			judge_ClassID()


print('Made "' + filename[1] + '.py" file in the output directory')