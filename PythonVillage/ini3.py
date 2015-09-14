#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Strings and Lists 
Rosalind/Python Village 
URL: http://rosalind.info/problems/ini3/
solution by James Hu@Tue
'''
import sys

def main():
    with open("ini3.in") as f:
        s = f.readline().strip()
        a, b, c, d = map(int, f.readline().strip().split())
        sys.stdout = open("ini3.out", "w")
        print s[a:b + 1], s[c:d + 1]

if __name__ == '__main__':
    main()
