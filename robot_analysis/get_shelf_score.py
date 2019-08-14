# encoding='utf-8'
import re
import pandas as pd

'''with open('athena-2019-07-08-09-1.txt', 'r', encoding='utf-8') as f:
    print(f.readlines())
    for s in f.readlines():
        print(s)
'''


def get_file_all_lines():
    with open(r"d:/software/athena-2019-07-08-09-1.log", "r", encoding='utf-8') as f:
        '''for line in f.readlines():
            print(line, end='')'''
        return f.readlines()


def get_map_shelf_score():
    lines = get_file_all_lines()
    map = {}
    for line in lines:
        shelf_score_regex = re.compile("^.*\"shelfCode\":\"(\\S\\d+)\".*\"shelfScore\":(\\d+).*$")
        regex_match = shelf_score_regex.search(line)
        if regex_match:
            shelfCode = regex_match.group(1)
            shelfScore = regex_match.group(2)
            # print(shelfCode + ":" + shelfScore)
            # map.update(shelfCode,shelfScore)
            map[shelfCode] = shelfScore
    return map


if __name__ == '__main__':
    map = get_map_shelf_score()
    data = pd.DataFrame(map.values(), map.keys())
    print(data)
    # print(map)
    '''with open("score.csv", 'w', encoding='utf-8') as f:
        for k in map.keys():
            f.write(k + ',' + map.get(k))
            f.write('\n')'''
