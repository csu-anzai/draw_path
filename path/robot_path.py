from path.playback import *
import matplotlib.pyplot as plt
import numpy as np
import time

'''
   author: zhangyu
   method: 获取机器人的路径，按照箭头方向画出来
'''


# 获取机器人回放的路径
def get_robot_palyback_path(url, playback_id, robot_id):
    robot_events = get_robot_events(url, playback_id)
    e = robot_events[robot_events.robotId == robot_id]
    arr = np.array(e)
    x = list(arr[:, 1])
    # print(arr[:, ])
    y = list(arr[:, 2])
    points = list(zip(x, y))
    plt = draw_path(points)
    return plt


# 根据机器人的运动轨迹点画箭头图
def draw_path(points):
    xs, ys = zip(*points)
    x_max, x_min = max(xs), min(xs)
    y_max, y_min = max(ys), min(ys)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(xs, ys, s=50)
    for i in range(1, len(points)):
        A, B = points[i - 1], points[i]
        ax.annotate("", xy=(B[0], B[1]), xytext=(A[0], A[1]), arrowprops=dict(arrowstyle="->"))
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.grid()
    return plt
    # plt.show()
    # plt.tight_layout()


if __name__ == '__main__':
    url = 'http://127.0.0.1:8889'
    # 开始时间
    start = time.time()
    robot_id = 1291079
    project_id = 1
    playback_id = 79
    pic = get_robot_palyback_path(url, playback_id, robot_id)
    pic.show()
    # 结束时间
    end = time.time()
    # 运行时间
    run_seconds_time = round(end - start, 2)
    print('程序运行长为:' + str(run_seconds_time) + '秒')
