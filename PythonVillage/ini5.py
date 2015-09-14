#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Working with Files 
Rosalind/Python Village 
URL: http://rosalind.info/problems/ini5/
solution by James Hu@Tue
'''
import sys

def main():
    with open("ini5.in") as f:
        sys.stdout = open("ini5.out", "w")
        for l in [l for idx, l in enumerate(f.readlines()) if idx % 2 == 1]:
            print l,

if __name__ == '__main__':
    main()
