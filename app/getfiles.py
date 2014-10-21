import os.path
import fnmatch
folder = 'to/'
path = '../mailbox/'+folder
count = 0
for root, dirnames, filenames in os.walk('../mailbox/'+folder):
		for filename in fnmatch.filter(filenames, '*.gpg'):
			count += 1

print count
