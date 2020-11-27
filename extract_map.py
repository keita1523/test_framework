

import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
import resource
import math

from itertools import groupby
# sys.setrecursionlimit(100000000)
# resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
# print(sys.getrecursionlimit())


def chagne_to_float(file):
	float_file = []
	for i in range(len(file)):
		float_row = []
		for j in range(len(file[i])):
			float_row.append(float(file[i][j]))
		float_file.append(float_row)

	return float_file

def chagne_to_int(file):
	int_file = []
	for i in range(len(file)):
		int_row = []
		for j in range(len(file[i])):
			int_row.append(int(file[i][j]))
		int_file.append(int_row)
	return int_file



def file_path(file_name):
	path = file_name
	with open(path, "r") as f:
		reader = csv.reader(f)
		csv_file = [row for row in reader]
	delete_first_row = np.delete(csv_file, 0, 0)
	float_format = chagne_to_float(delete_first_row)

	return float_format

def display(x,y):
	plt.plot(x,y)
	mpl.use('Agg')
	plt.savefig("hoge.png")


def lid_from_pid(line, point):

	x = []
	y = []
	X = 4
	Y = 5
	BPID = 1
	FPID = 2

	
	for l in range(len(line)):
		x.append(point[line[l][BPID]][X])
		y.append(point[line[l][BPID]][Y])
		x.append(point[line[l][FPID]][X])
		y.append(point[line[l][FPID]][Y])
	return x, y



def recursively_line3(file, ID, FLID, flid, index_array):
	index = []
	while file[flid][FLID] not in index_array:
		index.append(flid)
		index_array.append(flid)
		flid = file[flid][FLID]
	index.append(flid)

	return index, index_array


def connection_of_lid2(file, ID, B, F):
	index_array = [-1]
	connection_line_array = []
	i = 0
	flag = 0
	while flag < len(file):
		if flag not in index_array:
			connection_line = []
			if file[i][B] < 0:
				if file[i][F] < 0:
					index_array.append(file[i][ID])
					connection_line.append(file[i][ID])
				else:
					connection_line, index_array = recursively_line3(file, ID, F, file[i][ID], index_array)
					# connection_line = list(set(connection_line) - set(index_array))
					index_array.extend(connection_line)
			else:
				connection_line, index_array = recursively_line3(file, ID, F, file[i][ID], index_array)
				# connection_line = list(set(connection_line) - set(index_array))
				index_array.extend(connection_line)

			connection_line_array.append(connection_line)
		flag = flag + 1
		# print(i)
		i = i + 1
	return connection_line_array

def index_arrange(file, index):
	for i in range(len(file)):
		for j in range(len(index)):
			file[i][index[j]] = int(file[i][index[j]] - 1)
	return file

def extract_coordinate_and_display2(file, ID, PID, point, connection, judge_distance):

	X = 4
	Y = 5

	x_array = []
	y_array = []
	index_array = []
	for i in range(len(connection)):
	# for i in range(1):
		x = []
		y = []
		if len(connection[i]) == 1:
			pid = file[connection[i][0]][PID]
			x.append(point[pid][X])
			y.append(point[pid][Y])
		elif len(connection[i]) > 1:
			for j in range(len(connection[i])):
				pid = file[connection[i][j]][PID]
				x.append(point[pid][X])
				y.append(point[pid][Y])
		# if len(connection[i]) == 1:
		# 	pid = file[connection[i][0]][PID]
		# 	if judge_distance[pid] == True:
		# 		x.append(point[pid][X])
		# 		y.append(point[pid][Y])
		# elif len(connection[i]) > 1:
		# 	for j in range(len(connection[i])):
		# 		pid = file[connection[i][j]][PID]
		# 		if judge_distance[pid] == True:
		# 			x.append(point[pid][X])
		# 			y.append(point[pid][Y])
		plt.plot(x,y)

		index_array.append(len(x))
		x_array.append(x)
		y_array.append(y)
	mpl.use('Agg')
	plt.savefig("map.png")
	return x_array, y_array, index_array

def output_file():
	filename = "SanFrancisc"
	path = "./" + filename + ".m"
	with open(path, mode = 'w'):
		pass
	return path
def write_down(text, path):
	with open(path, mode = "a") as f:
		f.write(text)

def output_first_line(path):
	text = "scenario = drivingScenario\n"
	write_down(text, path)

def output_coordinate(index, x, y, path, last):
	# if last == True:
	# 	text = "    " + str(x) + " " + str(y) + " 0];\n"
	# 	write_down(text, path)
	# elif index % 15 == 0:
	# 	text = "    " + str(x) + " " + str(y) + " 0;\n"
	# 	write_down(text, path)
	if last == True:
		text = "    " + str(x) + " " + str(y) + " 0];\n"
		write_down(text, path)
	else:
		text = "    " + str(x) + " " + str(y) + " 0;\n"
		write_down(text, path)

def output_road(x, y, index, path):
	for i in range(len(index)):
	# for i in range(1):
		write_down("roadCenters = [...\n", path)
		for j in range(index[i]):
			# if j % 2 == 0:
			if j == index[i] - 1:
				last = True
			else:
				last = False
			output_coordinate(j, x[i][j], y[i][j], path, last)
		write_down("laneSpecification = lanespec(1, 'Width', 2);\n", path)
		write_down("road(scenario, roadCenters, 'Lanes', laneSpecification);\n", path)


def output_last_line(path):
	text = "drivingScenarioDesigner(scenario)\n"
	write_down(text, path)

def output_driving_scenario(x, y, index, path):
	output_first_line(path)
	output_road(x, y, index, path)
	output_last_line(path)

def distance(point_from, point_to):
	distance = point_to - point_from
	return np.linalg.norm(distance)

def judge_waypoint(d1, d2, d3):
	if math.isclose(d1 + d2, d3, rel_tol = 0.1) or d3 < math.sqrt(2) * d1:
		return not True
	else:
		return not False

def search_intersection_waypoint(x, y, index):
	judge_array = []
	for i in range(len(index)):
		judge = []
		judge.append(False)
		for j in range(index[i] - 2):
			point1 = np.array([x[i][j], y[i][j]])
			point2 = np.array([x[i][j + 1], y[i][j + 1]])
			point3 = np.array([x[i][j + 2], y[i][j + 2]])
			dis1 = distance(point1, point2)
			dis2 = distance(point2, point3)
			dis3 = distance(point1, point3)
			judge.append(judge_waypoint(dis1, dis2, dis3))
		judge.append(False)
		judge_array.append(judge)
	return judge_array

def delete_waypoint(x, y, index, judge_array):
	x_array = []
	y_array = []
	index_array = []
	for i in range(len(index)):
		delete_x = []
		delete_y = []
		for j in range(index[i]):
			if judge_array[i][j] == False:
				delete_x.append(x[i][j])
				delete_y.append(y[i][j])
		x_array.append(delete_x)
		y_array.append(delete_y)
		index_array.append(len(delete_x))

	return x_array, y_array, index_array



def false_count(index, judge_array):
	for i in range(len(index)):
		count = 0
		for j in range(index[i]):
			if judge_array[i][j] == True:
				count = count + 1
			if count % 15 == 0:
				judge_array[i][j] = False
	return judge_array

def search_continuous_waypoint(index, judge_array):
	all_false_index = []
	for i in range(len(index)):
		count = 0
		false_index_array = []
		check_continuous = False
		for j in range(index[i]):
			if check_continuous == True:
				if judge_array[i][j] == True:
					check_continuous = False
					end_index = j - 1
					false_index = [start_index, end_index, end_index - start_index]
					false_index_array.append(false_index)
			else:
				if judge_array[i][j] == False:
					start_index = j
					check_continuous = True
			# false_index_array.append([])
		all_false_index.append(false_index_array)

	return false_index_array


def reverse_true_false(judge_array):
	new_judge_array = []


	return new_judge_array

def group_by_TF(judge_array):
	group_array = []
	for i in range(len(judge_array)):
		out = [len([*group]) for j, group in groupby(judge_array[i])]
		group_array.append(out)
	return group_array

def import_False(judge, group_num, sum_waypoint_num, straight_lane):
	if straight_lane == 1:
		judge[sum_waypoint_num] = False
		judge[sum_waypoint_num + group_num - 1] = False
	elif group_num > 500:
		judge[sum_waypoint_num] = False
		judge[sum_waypoint_num + 5] = False
		for i in range(group_num // 100):
			judge[sum_waypoint_num + i * 100]
		judge[sum_waypoint_num + group_num - 6] = False
		judge[sum_waypoint_num + group_num - 1] = False
	else:
		judge[sum_waypoint_num] = False
		judge[sum_waypoint_num + group_num - 1] = False
	return judge



def change_TF_in_group(group_array, judge_array):
	new_judge_array = []
	for i in range(len(group_array)):
		judge = [True] * len(judge_array[i])
		sum_waypoint_num = 0
		for j in range(len(group_array[i])):
			if j % 2 == 0:
				judge = import_False(judge, group_array[i][j], sum_waypoint_num, len(group_array[i]))
				sum_waypoint_num = sum_waypoint_num + group_array[i][j]
			else:
				sum_waypoint_num = sum_waypoint_num + group_array[i][j]
		new_judge_array.append(judge)
	return new_judge_array

def reverse_judge_array(judge_array):
	group_array = group_by_TF(judge_array)
	new_judge_array = change_TF_in_group(group_array, judge_array)
	return new_judge_array

def smart_waypoint(x, y, index):


	x_array = []
	y_array = []
	judge_array = search_intersection_waypoint(x, y, index)
	# reverse_true_false(judge_array)
	judge_array =  reverse_judge_array(judge_array)
	false_index = search_continuous_waypoint(index, judge_array)

	x_array, y_array, new_index = delete_waypoint(x, y, index, judge_array)
	
	return x_array, y_array, new_index


def for_debag_output_file(filename, file):
	path = "./" + filename 
	with open(path, mode = 'w') as f:
		for i in range(len(file)):
			for j in range(len(file[i])-1):
				f.write(str(file[i][j]) + ",")
			f.write(str(file[i][-1]) + "\n")

# def for_debag_input_file(filename):
# 	path = "./" + filename
# 	csv = 
# 	with open(path, mode = 'r') as f:

# def file_path(file_name):
# 	path = "./" + file_name
# 	with open(path, "r") as f:
# 		reader = csv.reader(f)
# 		csv_file = [row for row in reader]
# 	delete_first_row = np.delete(csv_file, 0, 0)
# 	float_format = chagne_to_float(delete_first_row)

def for_debag_input_file(file_name):
	path = "./" + file_name
	with open(path, "r") as f:
		reader = csv.reader(f)
		csv_file = [row for row in reader]
	int_format = chagne_to_int(csv_file)
	return int_format

def check_same_waypoint(x, y, index):
	for i in range(len(index)):
		if x[i][0] == x[i][1] and y[i][0] == y[i][1]:
			print(i)

def rotate_coordinate(x, y, sin, cos):
	transform_x = x * cos - y * sin
	transform_y = x * sin + y * cos
	return transform_x, transform_y


def transform_coordinate(point, origin):
	X = 4
	Y = 5
	deg = np.deg2rad(180)
	cos = np.cos(deg)
	sin = np.sin(deg)
	max_dis = 300
	judge_distance = []
	
	for i in range(len(point)):
		transform_x = point[i][X] + origin[0]
		transform_y = point[i][Y] - origin[2]
		transform_x, transform_y = rotate_coordinate(transform_x, transform_y, sin, cos)
		point[i][X] = transform_x
		point[i][Y] = transform_y

		judge_distance.append(True if distance(np.zeros(2), np.array([transform_x, transform_y])) < max_dis else False)
		# print(np.array(transform_x, transform_y), distance(np.zeros(2), np.array(transform_x, transform_y)), judge_distance[i])
		# popo = np.array([transform_x, transform_y])
		# print(popo[0], popo[1])

	return point, judge_distance

def connection_line_considering_judge_distance(connection, PID, judge_distance):

	new_connection_line_array = []
	for i in range(len(connection)):
	# for i in range(1):
		new_connection_line = []
		print(len(new_connection_line))
		for j in range(len(connection[i])):
			if judge_distance[connection[i][j]] == True:
				new_connection_line.append(connection[i][j])
			# elif len(new_connection_line) == 0:
			# 	continue
			elif len(new_connection_line) >= 2:
				new_connection_line_array.append(new_connection_line)
				new_connection_line = []
				# print("pep\n", new_connection_line_array)

	# print(new_connection_line_array)
	return new_connection_line_array



# def extract_coordinate_and_display2(file, ID, PID, point, connection, judge_distance):

# 	X = 4
# 	Y = 5

# 	x_array = []
# 	y_array = []
# 	index_array = []
# 	for i in range(len(connection)):
# 	# for i in range(1):
# 		x = []
# 		y = []
# 		if len(connection[i]) == 1:
# 			pid = file[connection[i][0]][PID]
# 			x.append(point[pid][X])
# 			y.append(point[pid][Y])
# 		elif len(connection[i]) > 1:
# 			for j in range(len(connection[i])):
# 				pid = file[connection[i][j]][PID]
# 				x.append(point[pid][X])
# 				y.append(point[pid][Y])

def adapt_for_matlab_environment(x, y, index):
	deg = np.deg2rad(-90)
	cos = np.cos(deg)
	sin = np.sin(deg)

	for i in range(len(index)):
		for j in range(index[i]):
			transform_x, transform_y = rotate_coordinate(x[i][j], y[i][j], sin, cos)
			transform_y = -1 * transform_y
			x[i][j] = transform_x
			y[i][j] = transform_y
	return x, y

def main():

	PID = 0
	LID = 0
	BPID = 1
	FPID = 2
	BLID = 3
	FLID = 4

	DID = 0
	D_PID = 2 # dtlane PID
	LnID = 0
	Ln_DID = 1
	Ln_BLID = 2 # lane.csv BLID
	Ln_FLID = 3

	origin_point = [-201.879058837891, 10.2880001068115, 217.720001220703]

	point = file_path("/home/saitama1/autoware-data/SanFrancisco/data/map/vector_map/point.csv")
	arrange = [PID]
	point = index_arrange(point, arrange)
	point, judge_distance = transform_coordinate(point, origin_point)
	# print(judge_distance)
	print("point")
	
	line = file_path("/home/saitama1/autoware-data/SanFrancisco/data/map/vector_map/line.csv")
	arrange = [LID, BPID, FPID, BLID, FLID]
	line = index_arrange(line, arrange)
	print("line")

	dtlane = file_path("/home/saitama1/autoware-data/SanFrancisco/data/map/vector_map/dtlane.csv")
	arrange = [DID, D_PID]
	dtlane = index_arrange(dtlane, arrange)
	print("dtlane")
	

	lane = file_path("/home/saitama1/autoware-data/SanFrancisco/data/map/vector_map/lane.csv")
	arrange = [LnID, Ln_DID, Ln_BLID, Ln_FLID]
	lane = index_arrange(lane, arrange)
	print("lane")

	# connection_line = connection_of_lid2(lane, LnID, Ln_BLID, Ln_FLID)
	# print(connection_line)
	# for_debag_output_file("connection_line", connection_line)
	# print("connection_line")

	connection_line = for_debag_input_file("connection_line")
	print(len(connection_line[0]))

	connection_line = connection_line_considering_judge_distance(connection_line, D_PID, judge_distance)
	print(len(connection_line[0]))
	# for i in range(len(connection_line)):
	# 	for j in range(len(connection_line[i])):

	# 		print(point[connection_line[i][j]][4], point[connection_line[i][j]][5], judge_distance[connection_line[i][j]])


	x, y, index = extract_coordinate_and_display2(dtlane, DID, D_PID, point, connection_line, judge_distance)
	print(x)
	x, y = adapt_for_matlab_environment(x, y, index)
	# x, y, index = smart_waypoint(x, y, index)

	check_same_waypoint(x, y, index)

	print("extract x y")

	path = output_file()

	output_driving_scenario(x, y, index, path)
	print("output")










if __name__ == '__main__':
	main()
