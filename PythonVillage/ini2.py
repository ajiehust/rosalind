#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Variables and Some Arithmetic 
Rosalind/Python Village 
URL: http://rosalind.info/problems/ini2/
solution by James Hu@Tue
'''
import sys

def main():
    with open("ini2.in") as f:
        x, y = map(int, f.readline().strip().split())
        sys.stdout = open("ini2.out", "w")
        print x ** 2 + y ** 2

if __name__ == '__main__':
    main()
