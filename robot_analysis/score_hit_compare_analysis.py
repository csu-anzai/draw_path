# encoding='utf-8'
from path.playback import *
import matplotlib.pyplot as plt
import time

'''
   method: 货架分数命中比较图
   time:2019.7.8
'''


# 分数命中对比表（不准确）
def get_score_hit_compare(url, playback_Id):
    shelf_events = get_shelf_event(url, playback_Id)
    load_events = shelf_events[shelf_events.action == 'load']
    # 查询货架被顶起的数量
    shelf_hits = load_events.groupby("shelfCode").size()
    shelf_hits_df = pd.DataFrame(shelf_hits)
    # 从日志中抓或者而不是读取文件
    pred_hot_shelves = pd.read_csv("score.csv", header=None, index_col=0)
    print(pred_hot_shelves)
    pd.read_
    cross = pd.concat([shelf_hits_df, pred_hot_shelves.round()], axis=1)
    cross = cross.fillna(0)
    cross.columns = ["hit", "score"]
    plt.figure(figsize=(10, 10))
    plt.xlabel('Hit Number')
    plt.ylabel('Predict Score')
    plt.scatter(cross["hit"], cross["score"])
    return plt


if __name__ == '__main__':
    url = 'http://127.0.0.1:8889'
    # 开始时间
    start = time.time()
    project_id = 1
    playback_id = 83
    pic = get_score_hit_compare(url, playback_id)
    pic.title("2019-7-8 9:00:00")
    pic.savefig(r"D:\code\draw_path\dispaly_pic\html\score_hit_analysis.jpg")
    pic.show()
    # 结束时间
    end = time.time()
    # 运行时间
    run_seconds_time = round(end - start, 2)
    print('程序运行长为:' + str(run_seconds_time) + '秒')
