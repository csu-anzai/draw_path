encoding = 'utf-8'
import shelve

'''s = shelve.open('test_s.db', flag='r')
print(s['k1'])
s['k2']=[1,2,3]
print(s['k2'])
s.close()'''

s=shelve.open('test_s.db',flag='c')
print(s.keys())
print(len(s))
s['k2']=(33,44)
print(s)
print(s['k2'])