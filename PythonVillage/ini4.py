#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Conditions and Loops 
Rosalind/Python Village 
URL: http://rosalind.info/problems/ini4/
solution by James Hu@Tue
'''
import sys

def main():
    with open("ini4.in") as f:
        a, b = map(int, f.readline().strip().split())
        sys.stdout = open("ini4.out", "w")
        print sum([i for i in range(a, b + 1) if i % 2 == 1])

if __name__ == '__main__':
    main()
