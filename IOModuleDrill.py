import os

"""
Windows os won't understand the absolute file path as a string.
Have to use the methods below so Windows understands the absolute path
"""

fname = 'test.txt' #file name

fpath = 'C:\\python_projects\\' #use the escape so Python knows.

abpath = os.path.join(fpath, fname) #abpath means absolute path
print(abpath)


