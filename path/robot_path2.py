encoding = 'utf-8'
from path.playback import *
import matplotlib.pyplot as plt
import time
import numpy as np

'''
   author:zhangyu
   method: 获取机器人的路径，按照三角形方向画出来
'''


# 获取单个机器人走的轨迹
def get_single_robot_path(url, playback_id, robot_id):
    robot_events = get_robot_events(url, playback_id)
    e = robot_events[robot_events.robotId == robot_id]
    arr = np.array(e)
    x = list(arr[:, 1])
    y = list(arr[:, 2])
    points = list(zip(x, y))
    plt.scatter(points[0][0], points[0][1], c='r', marker='o')
    # 按照方向打印机器人的路径
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
    # project_id = 1
    playback_id = 79
    robot_id = 1291079
    # 开始时间
    start = time.time()
    pic = get_single_robot_path(url, playback_id, robot_id)
    # 展示图片
    pic.show()
    # 结束时间
    end = time.time()
    # 运行时间
    run_seconds_time = round(end - start, 2)
    print('程序运行长为:' + str(run_seconds_time) + '秒')
