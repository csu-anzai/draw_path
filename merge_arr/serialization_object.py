# encoding='utf-8'

import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d)
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)


with open('dump.txt','rb') as f:
    d1=pickle.load(f)
    print(d1)
