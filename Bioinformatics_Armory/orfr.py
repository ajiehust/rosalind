#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Finding Genes with ORFs 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/orfr/
solution by James Hu@Tue
'''
import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

def trim(seq):
    r = len(seq) % 3
    if r==0: return seq
    else: return seq[:-r]

def main():
    seq = Seq(open("orfr","rU").read().strip(), generic_dna)
    result = [trim(seq[i:]) for i in range(3)]
    result += map(Seq.reverse_complement, result)
    result = reduce(lambda x,y: x+y, map(lambda s:str(s.translate(table=1)).split("*"), result))
    result = sorted(result, key = len)
    sys.stdout = open("orfr.out", "w")
    print result[-1]
if __name__ == '__main__':
    main()
