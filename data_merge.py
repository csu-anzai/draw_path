# encoding='utf-8'
'''
   author:zhangyu
   date:2019.8.22
   description:测试dataframe的合并
'''

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''data1 = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K2', 'K3']
}
left = DataFrame(data1, columns=['A', 'B', 'key'],
                 index=[0, 1, 2, 3])
data2 = {
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'key': ['K0', 'K1', 'K2', 'K3']
}
right = DataFrame(data2, columns=['C', 'D', 'key'],
                  index=[0, 1, 2, 3])
'''
# print(right)

# result1 = pd.merge(left, right, on='key')
# print(result1)

'''
# 测试merge
result2=pd.merge(left,right,how='left',on=['key','key'])
print(result2)
'''

data1 = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}
df1 = DataFrame(data1, columns=['A', 'B', 'C', 'D'],
                index=[0, 1, 2, 3])

data2 = {
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
}
df2 = DataFrame(data2, columns=['A', 'B', 'C', 'D'],
                index=[4, 5, 6, 7])

'''result=df1.append(df2)
print(result)'''

'''data1 = {
    'A': ['A0', 'A1','A2'],
    'B': ['B0', 'B1','B2']
}
left = DataFrame(data1, columns=['A', 'B'], index=['K0', 'K1', 'K2'])
data2 = {
    'C': ['C0', 'C1','C2'],
    'D': ['D0', 'D1','D2']
}
right = DataFrame(data1, columns=['C', 'D'], index=['K0', 'K2', 'K3'])
result=left.join(right)
print(result)'''

# cancat

frames = [df1, df2]
result = pd.concat(frames)
# print(result)

result1=pd.concat(frames, keys=['x', 'y'])
print(result1.ix['y'])