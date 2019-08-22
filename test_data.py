# encoding='utf-8'

'''
   author:zhangyu
   date:2019.8.21
   description:测试dataframe
'''

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data={
    '省份':['北京','上海','天津','重庆','江苏','浙江','广东'],
    '年份':[2017,2018,2016,2018,2016,2017,2015],
    '总人数':[222,333,567,360,303,267,901],
    '高考人数':[60.12,3.15,20.14,24.68,2.13,6.19,9.02]
}
frame1=DataFrame(data,columns=['年份','省份','总人数','高考人数'],
                 index=['one','two','three','four','five','six','seven'])

#print(frame1)

#print(frame1[1:4])

#print(frame1[frame1.总人数>300])

#print(frame1.ix['one'])

#print(frame1.ix[:2])

#print(frame1.iloc[2,])

#print(frame1.iloc[2:4,])

#print(frame1.loc['two'])

print(frame1.loc['two':'three'])