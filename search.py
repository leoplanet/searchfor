#!/usr/bin/python -tt

import sys
import os
import re

# Define a main() function that prints a little greeting.
def main():
  print 'Path given -->', sys.argv[1], '\n'
  parsedir(sys.argv[1])

def parsedir(searchdir):
  filecount = 0
  found = ''
  for root, subfolder, files in os.walk(searchdir):
    #print root, subfolder, files, "\n"
    for file in files:
      fullpath = os.path.join(root,file)
      filecount += 1
      #print fullpath, "\n"
      filestring = search_extension(fullpath)
      found = search_file(filestring)
      if found == 'True':
        print fullpath, "\n"
  print 'Total number of files --> %d' %filecount

def search_extension(fullpath):
  with open(fullpath, "r") as f:
    readfile = ""
    (filepath,extension) = os.path.splitext(fullpath)
    if extension in ['.txt','.doc']:
      readfile = f.read()
      #print fullpath, "\n"
      #print readfile
    return readfile

def search_file(filestring):
  match = re.search(r'leo',filestring)
  if match:
    print match.group()
    return 'True'
  else:
    return 'False'



if __name__ == '__main__':
  main()
