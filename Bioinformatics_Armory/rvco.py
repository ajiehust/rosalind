#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Complementing a Strand of DNA 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/rvco/
solution by James Hu@Tue
'''
import sys
from Bio import SeqIO

def main():
    fasta = list (SeqIO.parse(open("rvco"), "fasta"))
    sys.stdout = open("rvco.out", "w")
    print sum([seq.seq == seq.reverse_complement().seq for seq in fasta])

if __name__ == '__main__':
    main()

