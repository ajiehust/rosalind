#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Read Quality Distribution 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/phre/
solution by James Hu@Tue
'''
import sys
from Bio import SeqIO

def main():
    with open("phre") as f:
        threshold = int(f.readline().strip())
        fastq = [rcd.letter_annotations["phred_quality"] for rcd in SeqIO.parse(f, "fastq")]
        sys.stdout = open("phre.out", "w")
        print sum([1 for rcd in fastq if float(sum(rcd)) / len(rcd) < threshold])

if __name__ == '__main__':
    main()
