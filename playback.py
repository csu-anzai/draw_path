import requests
import re
# _*_ coding: utf-8 _*_
import pandas as pd
import json

ROBOT_EVENT = 'robotevents'
ROBOT_PATH = 'robotpath'
TASK_EVENT = 'taskevents'
SHELF_EVENT = 'shelfevents'

def get_map(url, projectId):
    new_url = url + '/project/getMap' +  '?id=' + str(projectId) 
    r = requests.get(new_url)
    data = json.loads(r.content)
    data = data['data']
    return data

def get_events(url, event, playbackId, robotId = 0, time = 0):
    new_url = url + '/metrics/' + event + '?id=' + str(playbackId) + '&robotId=' + str(robotId) + "&time=" + str(time)
    r = requests.get(new_url)
    return r

def get_robot_events(url, playbackId):
    r = get_events(url, ROBOT_EVENT, playbackId)
    data = json.loads(r.content)
    data = data['data']
    return pd.DataFrame(data, columns=['robotId', 'x', 'y', 'time'])

def get_robot_path(url, playbackId, robotId, time=0):
    r =  get_events(url, ROBOT_PATH, playbackId, robotId, time)
    data = json.loads(r.content)
    data = data['data']
    return pd.DataFrame(data, columns=['time', 'x', 'y', 'z'])

def get_task_event(url, playbackId):
    r = get_events(url, TASK_EVENT, playbackId)
    data = json.loads(r.content)
    data = data['data']
    return pd.DataFrame(data, columns=['taskId', 'action', 'taskType', 'robotId', 'stationId','shelfCode', 'time'])

def get_shelf_event(url, playbackId):
    r =  get_events(url, SHELF_EVENT, playbackId)
    data = json.loads(r.content)
    data = data['data']
    return pd.DataFrame(data, columns=['shelfCode', 'robotId', 'action', 'x','y','z','taskId', 'time'])