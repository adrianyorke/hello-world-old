#!/usr/bin/env python
"""Module docstring [pylint-C0111]."""

import csv
import chardet

def detect_encoding():
    with open(r'H:\Documents\Projects\2017.08 Python CSV\tapahtumat20161201-20170826.csv', 'rb') as f:
        content = f.read()

    print chardet.detect(content)
    return chardet.detect(content)['encoding']

def reencode(f, encoding_detected):
    for line in f:
        #yield line.decode('ISO-8859-1').encode('utf-8')
        #yield line.decode('windows-1250').encode('utf-8')
        yield line.decode(encoding_detected).encode('utf-8')

def main():
    print u'\xe4' # ä
    print u'\xf6' # ö
    
    encoding_detected = detect_encoding()

    with open(r'H:\Documents\Projects\2017.08 Python CSV\tapahtumat20161201-20170826.csv', 'rb') as csvfile:
        content = csv.reader(csvfile, delimiter=';', quotechar='"')

        for row in content:
            #row.decode('windows-1250').encode('utf-8')
            #print ' ~ '.join(reencode(row, encoding_detected))
            print row

if __name__ == '__main__':
    main()
