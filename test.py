import os,sys

enter=input('')
argslist=enter.split(' ')
print(argslist[3])
print(os.path.exists(argslist[3]))
