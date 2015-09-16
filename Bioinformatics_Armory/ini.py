#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Introduction to the Bioinformatics Armory
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/ini/
solution by James Hu@Tue
'''
import sys
def main():
    with open("ini") as f:
        seq = f.readline().strip()
        sys.stdout = open("ini.out","w")
        print " ".join(map(str, [seq.count(x) for x in ['A','C','G','T']]))

if __name__ == '__main__':
    main()
