#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Protein Translation 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/ptra    /
solution by James Hu@Tue
'''
import sys
from Bio.Seq import translate

def main():
    with open("ptra") as f:
        dna, aa = f.read().strip().split("\n")
    sys.stdout = open("ptra.out", "w")
    for code_var in range(1, 7) + range(9, 16):
        if translate(dna, table=code_var, to_stop=True) == aa:
            print code_var,

if __name__ == '__main__':
    main()
