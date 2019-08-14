import requests
import re
# _*_ coding: utf-8 _*_
import pandas as pd
import json

ROBOT_EVENT = 'robotevents'
ROBOT_PATH = 'robotpath'
TASK_EVENT = 'taskevents'
SHELF_EVENT = 'shelfevents'


# 获取地图信息
def get_map(url, projectId):
    new_url = url + '/project/getMap' + '?id=' + str(projectId)
    r = requests.get(new_url)
    data = json.loads(r.content)
    data = data['data']
    return data


# 获取任务事件信息
def get_events(url, event, playbackId, robotId=0, time=0):
    new_url = url + '/metrics/' + event + '?id=' + str(playbackId) + '&robotId=' + str(robotId) + "&time=" + str(time)
    r = requests.get(new_url)
    return r

def get_events(url, event, playbackId):
    new_url = url + '/metrics/' + event + '?id=' + str(playbackId)
    r = requests.get(new_url)
    return r

# 获取机器人事件信息
def get_robot_events(url, playbackId):
    r = get_events(url, ROBOT_EVENT, playbackId)
    data = json.loads(r.content)
    # print(data)
    data = data['data']
    return pd.DataFrame(data, columns=['robotId', 'x', 'y', 'time'])


# 获取机器人路径信息
def get_robot_path(url, playbackId, robotId, time=0):
    r = get_events(url, ROBOT_PATH, playbackId, robotId, time)
    data = json.loads(r.content)
    data = data['data']
    return pd.DataFrame(data, columns=['time', 'x', 'y', 'z'])


# 获取任务事件
def get_task_event(url, playbackId):
    r = get_events(url, TASK_EVENT, playbackId)
    data = json.loads(r.content)
    data = data['data']
    return pd.DataFrame(data, columns=['taskId', 'action', 'taskType', 'robotId', 'stationId', 'shelfCode', 'time'])


# 获取货架事件
def get_shelf_event(url, playbackId):
    r = get_events(url, SHELF_EVENT, playbackId)
    data = json.loads(r.content)
    data = data['data']
    return pd.DataFrame(data, columns=['shelfCode', 'robotId', 'action', 'x', 'y', 'z', 'taskId', 'time'])
