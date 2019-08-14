encoding = 'utf-8'
import shelve

s = shelve.open('test_s.db')  # 创建shelve并打开
s['k1'] = {'int': 10, 'float': 8.8, 'string': 'python'}  # 写入数据
s.close()  # 关闭文件
s = shelve.open('test_s.db')  # 打开文件
print(s['k1'])  # 访问shelve中的数据
print(s['k1']['int'])
s.close()
