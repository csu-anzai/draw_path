from playback import *
import matplotlib.pyplot as plt
import time
import os
import numpy as np
import seaborn as sns


def get_single_robot_path(url, playback_id, robot_id):
    robot_events = get_robot_events(url, playback_id)
    e = robot_events[robot_events.robotId == robot_id]
    arr = np.array(e)
    '''save = pd.DataFrame(e)
    robot_location = 'robot_' + str(robot_id) + '_' + str(playback_id) + '.csv'
    file_exist_flag = os.path.exists(robot_location)
    if file_exist_flag != True:
        save.to_csv(robot_location)  # index=False,header=False表示不保存行索引和列标题
    df = pd.read_csv(robot_location)  # .rename(columns={'Unnamed: 0': 'robot_id'})
    '''
    x = list(arr[:, 1])
    y = list(arr[:, 2])
    points = list(zip(x, y))
    plt.scatter(points[0][0], points[0][1], c='r', marker='o')
    for i in range(1, len(points) - 1):
        A, B = points[i - 1], points[i]
        if A[0] < B[0] and A[1] == B[1]:
            plt.scatter(points[i][0], points[i][1], c='black', marker='>')
        if A[0] == B[0] and A[1] < B[1]:
            plt.scatter(points[i][0], points[i][1], c='black', marker='^')
        if A[0] > B[0] and A[1] == B[1]:
            plt.scatter(points[i][0], points[i][1], c='black', marker='<')
        if A[0] == B[0] and A[1] > B[1]:
            plt.scatter(points[i][0], points[i][1], c='black', marker='v')
    plt.scatter(points[len(points) - 1][0], points[len(points) - 1][1], c='r', marker='x')
    return plt


if __name__ == '__main__':
    url = 'http://127.0.0.1:8889'
    project_id = 1
    playback_id = 79
    robot_id = 1291079
    start = time.time()
    pic = get_single_robot_path(url, playback_id, robot_id)
    pic.show()
    end = time.time()
    print(end - start)
