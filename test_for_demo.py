# encoding='utf-8'

name = '1234567'

'''for ch in name:
    print(ch)'''

'''for index, every_char in enumerate(name):
    print(str(index) + ":" + every_char)'''

for every_char in iter(name):
    print(every_char)
