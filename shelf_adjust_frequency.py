# encoding='utf-8'

from playback import *
import matplotlib.pyplot as plt
import numpy as np
import time

# import seaborn as sns
'''
   author:zhangyu
   date:2019.8.13
   description: 统计下迪卡侬电商最近货架调整的频率（2019-8-7~2019-8-8）
'''


# shelf_code:C000526   K000239   A000278
def statistic_shelf_move_frequency(shelf_code):
    url = 'http://172.16.8.90:8888'
    playbackId = 59
    shelf_events = get_shelf_event(url, playbackId)
    load_events = shelf_events[shelf_events.action == 'load']
    # print(load_events)
    same_shelf = load_events[load_events.shelfCode == shelf_code]
    # print(same_shelf)
    shelf_move_group = same_shelf.groupby(["x", "y"]).size()
    # print(shelf_move_group)
    move_number = len(shelf_move_group)
    # 每个货架搬运的次数
    return move_number / 24


if __name__ == '__main__':
    start = time.clock()
    move_number = statistic_shelf_move_frequency('C000526')
    end = time.clock()
    print(round(move_number, 2))
    print("运行了" + str(round(end - start, 2)) + "秒")
