from playback import *
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns


def get_robot_palyback_path(url, playback_id, robot_id):
    robot_events = get_robot_events(url, playback_id)
    e = robot_events[robot_events.robotId == robot_id]
    arr = np.array(e)
    col = list(arr[:, 1])
    print(col)
    for k in arr:
        print(int(k[0]))
        print(k[1])

if __name__ == '__main__':
    url = 'http://127.0.0.1:8889'
    robot_id = 1291079
    project_id = 1
    playback_id = 79
    get_robot_palyback_path(url, playback_id, robot_id)
