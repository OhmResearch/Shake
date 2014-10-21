import os
import sys


fileList = []
rootdir = '../mailbox/from'
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        fileList.append(os.path.join(root,file))
	print os.path.join(root,file)
    	
#print fileList
