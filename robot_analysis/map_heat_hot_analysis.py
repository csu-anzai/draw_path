# encoding='utf-8'

from path.playback import *
import matplotlib.pyplot as plt
import numpy as np

'''
   method: 地图命中热度图
   time: 2019.7.8
'''


# 分析地图的热度
def map_heat_hot_pic(url, playback_id):
    robot_events = get_robot_events(url, playback_id)
    m = np.zeros([70, 70])
    for k in np.array(robot_events):
        x = int(k[1]) - 70
        y = int(k[2]) - 10
        if x < 70 and y < 70:
            m[y][x] = m[y][x] + 1
    station_pos = {1: (67, 22), 2: (67, 28), 3: (67, 31), 4: (67, 35), 5: (67, 40), 6: (67, 43)}
    plt.figure(figsize=(20, 10))
    plt.ylabel('y')
    plt.xlabel('x')
    plt.imshow(m, origin='lower')
    for i in range(1, 7):
        plt.text(int(station_pos[i][0] * 1.15 - 70), int(station_pos[i][1] * 1.35 - 10), 'S' + str(i), color='white')
    return plt


if __name__ == '__main__':
    # url = 'http://172.16.8.90:8888'
    url = 'http://127.0.0.1:8889'
    playback_id = 83
    # print(robot_events)
    pic = map_heat_hot_pic(url, playback_id)
    fig = pic.gcf()
    fig.set_size_inches(40, 40)
    fig.savefig(r"D:\code\draw_path\dispaly_pic\html\map_hot_pic.jpg", dpi=40)
    pic.show()
