from playback import *
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns

def get_robot_palyback_path(url, playback_id, robot_id):
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
    plt = draw_path(points)
    return plt


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
    robot_id = 1291079
    project_id = 1
    playback_id = 79
    pic = get_robot_palyback_path(url, playback_id, robot_id)
    pic.show()
