import os
import re
import pprint
import chardet

def detect_encoding(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()

    print chardet.detect(content)
    return chardet.detect(content)['encoding']

mypath = r'C:\Temp'
f = []
for (dirpath, dirnames, filenames) in os.walk(mypath):
    #f.extend(filenames)
    #f.extend(os.path.join(dirpath, filenames))
    #f += filenames
        #f += os.path.join(dirpath, filenames)
    #f.extend(filenames)
    for filename in filenames:
        print filename
        if re.search(r'.txt$', filename, flags=0):
            print detect_encoding(os.path.join(dirpath, filename))
    break

pprint.pprint(f)
