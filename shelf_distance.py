encoding = 'utf-8'
from playback import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import time

url = 'http://172.16.8.90:8888'
projectId = 1
playbackId = 55

start_time = time.time()


def get_manhattan_distance(p1, p2):
    distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return distance


robot_events = get_robot_events(url, playbackId)
robot_events_arr = np.array(robot_events)
# print(len(robot_events_arr[:, 0]))

robot_id1 = list(robot_events_arr[:, 0])
x = list(robot_events_arr[:, 1])
y = list(robot_events_arr[:, 2])
time1 = list(robot_events_arr[:, 3])
# print(time1)
robot_events_tuple = zip(robot_id1, x, y, time1)
robot_events_result = sorted(robot_events_tuple, key=lambda s: s[3])
# print(robot_events_result)
'''for event in robot_events_tuple:
    print(int(event[0]))
    print(event[1])
    print(event[2])
    print(int(event[3]))'''
shelf_events = get_shelf_event(url, playbackId)
# load_events = shelf_events[shelf_events.action == 'load']
# 查询货架被顶起的数量
shelf_hits = shelf_events.groupby("shelfCode").size()
shelf_hits_df = pd.DataFrame(shelf_hits)
shelf_events_arr = np.array(shelf_events)
robot_id2 = list(shelf_events_arr[:, 1])
time2 = list(shelf_events_arr[:, 7])
action = list(shelf_events_arr[:, 2])
shelf_code = list(shelf_events_arr[:, 0])
shelf_events_tuple = zip(shelf_code, robot_id2, action, time2)
shelf_events_result = sorted(shelf_events_tuple, key=lambda s: s[3])
# print(shelf_events_result)
arr2 = []
for i in range(len(shelf_events_result) - 1):
    for j in range(i + 1, len(shelf_events_result)):
        if shelf_events_result[i][0] == shelf_events_result[j][0] and int(shelf_events_result[j][1]) == 0:
            arr1 = []
            arr1.append(shelf_events_result[i][3])  # 开始时间
            arr1.append(shelf_events_result[j][3])  # 结束时间
            arr1.append(shelf_events_result[i][1])  # robot_id
            if shelf_events_result[i][1] != 0:
                arr2.append(arr1)
                break
print(len(arr2))
print(arr2)
'''for shelf_event in shelf_events_result:
    for robot_event in robot_events_result:
        if int(robot_event[0]) == int(shelf_event[0]):
            print(robot_event[1], end=' ')
 
           print(robot_event[2])'''

location2 = []
for arr in arr2:
    location1 = []
    for robot_event in robot_events_result:
        robot_id = int(arr[2])
        start_time = int(arr[0])
        end_time = int(arr[1])
        if robot_id == int(robot_event[0]) and start_time <= robot_event[3] and end_time >= robot_event[3]:
            location_arr = []
            x = robot_event[1]
            y = robot_event[2]
            location_arr.append(x)
            location_arr.append(y)
            location1.append(location_arr)
    location2.append(location1)
print(location2)  # 所有的位置信息
sum = 0
for location_arr in location2:
    for index in range(0, len(location_arr) - 1):
        sum += get_manhattan_distance(location_arr[index], location_arr[index + 1])
print(sum)
end_time = time.time()
#print('程序运行' + str(end_time - start_time) + 's')
