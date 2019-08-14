encoding = 'utf-8'
import shelve

s = shelve.open('test_s.db', writeback=True)
print(s['k1'])
print(s['k2'])

s['k1']['float'] = 99.99
print(s['k1'])
