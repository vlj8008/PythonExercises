
import time
import shutil #stands for "shell utilities".
import os

seconds_in_day = 24*60*60

source = '/Users/vicky/OneDrive/Desktop/edited_files/'
destination = '/Users/vicky/OneDrive/Desktop/transfer_files/'

now = time.time() #returns time as a float expressing seconds since epoch in UTC
#epoch = point where time starts for Python which is 1 Jan 1970. UTC means Cordinated Universal Time
print(now)

path = '/Users/vicky/OneDrive/Documents/GitHub/Python Course/shutil_sub/edited_files/customer.txt/'



def last_mod_time(path):
    return os.path.getmtime(path) #returns seconds since epoch
    print(mod_time)


