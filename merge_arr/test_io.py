# encoding='utf-8'
import os

print(os.getcwd())
# os.mkdir('newdir')
# chdir进入某个目录下
# os.chdir('newdir')
#print(os.getcwd())
# os.rmdir("/tmp/test")
# os.rmdir('newdir')
#os.rmdir('tmp/test')
a=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(a)