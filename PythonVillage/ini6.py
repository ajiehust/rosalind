#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Dictionaries  
Rosalind/Python Village 
URL: http://rosalind.info/problems/ini6/
solution by James Hu@Tue
'''
import sys

def main():
    with open("ini6.in") as f:
        words = f.readline().strip().split()
        words = {w:words.count(w) for w in words}
        sys.stdout = open("ini6.out", "w")
        for k, v in words.iteritems():
            print "%s %d" % (k, v)

if __name__ == '__main__':
    main()
