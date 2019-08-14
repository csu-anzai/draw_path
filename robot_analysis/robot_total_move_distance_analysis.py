# encding='utf-8'
import numpy as np

'''
   method: 求任务总数和货架搬运的总距离,dist_x距离 dist_y距离 ，dist_x_y距离
   time:2019.7.5
'''

def get_robot_total_move_distance(robot_events, shelf_events):
    events = []
    for r in np.array(robot_events):
        events.append(["robot_events", r[3], str(r[0])[:-2], r[1], r[2]])
    for s in np.array(shelf_events):
        events.append(["shelf_events", s[7], s[0], s[1], s[2]])
    events = np.array(events)
    events = events[np.argsort(events[:, 1])]
    dist_x = 0.0
    dist_y = 0.0
    robot_shelf = {}
    shelf_robot = {}
    robot_last = {}
    load_event_count = 0
    unload_event_count = 0
    for e in events:
        if e[0] == "robot_events":
            robotId = e[2]
            if robotId in robot_shelf and robotId in robot_last:
                last = robot_last[robotId]
                dx = abs(float(last[1]) - float(e[4]))
                dy = abs(float(last[0]) - float(e[3]))
                if dx < 10:
                    dist_x = dist_x + dx
                if dy < 10:
                    dist_y = dist_y + dy
            robot_last[robotId] = (e[3], e[4])
        if e[0] == "shelf_events":
            if e[4] == "load" and e[3] != '0':
                robotId = e[3]
                shelfCode = e[2]
                shelf_robot[shelfCode] = robotId
                robot_shelf[robotId] = shelfCode
                load_event_count = load_event_count + 1
            elif e[4] == "unload":
                shelfCode = e[2]
                unload_event_count = unload_event_count + 1
                if shelfCode in shelf_robot:
                    robotId = shelf_robot[shelfCode]
                    shelf_robot.pop(shelfCode)
                    robot_shelf.pop(robotId)
    print("单次货架搬运（从顶升到放下）的x运动距离")
    avg_dist_x = dist_x / load_event_count
    print(avg_dist_x)
    print("单次货架搬运（从顶升到放下）的y运动距离")
    avg_dist_y = dist_y / load_event_count
    print(avg_dist_y)
    print("单次货架搬运（从顶升到放下）的运动距离")
    avg_dist_x_y = (dist_y + dist_x) / load_event_count
    print(avg_dist_x_y)
    return avg_dist_x, avg_dist_y, avg_dist_x_y


if __name__ == '__main__':
    robot_events=''
    shelf_events=''
    new_avg_dist_x, new_avg_dist_y, new_avg_dist_x_y =get_robot_total_move_distance(robot_events,shelf_events)