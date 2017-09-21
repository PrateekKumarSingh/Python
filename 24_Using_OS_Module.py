import os

print(os.getcwd()) # gets current working directory

root = '.\\Samplefiles\\' #'\' is the escape char
name = root+'testdir'
newname = root+'testdir2'
try :
    os.mkdir(name) # makes a new directory with name 'TestDir' 
    print('Creating directory {0} ..'.format(name))
except Exception as e:
    print(e)    

import time
time.sleep(2)

os.rename(name,newname) # os.rename() to rename a directory
print("Renaming the directory '{0}' to '{1}'".format(name,newname) )

print("Deleting the directory '{0}' ..".format(newname))
time.sleep(4)
os.rmdir(newname) # os.rmdir() to remove a directory

# to know more use help(os)