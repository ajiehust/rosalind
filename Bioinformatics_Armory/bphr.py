#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Base Quality Distribution 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/bphr/
solution by James Hu@Tue
'''
import sys
import numpy as np
from Bio import SeqIO

def main():
    with open("bphr") as f:
        threshold = int(f.readline().strip())
        fastq = np.array([rcd.letter_annotations["phred_quality"] for rcd in SeqIO.parse(f, "fastq")])
        fq = np.mean(fastq, axis=0)
    sys.stdout = open("bphr.out", "w")
    print len(fq[fq < threshold])

if __name__ == '__main__':
    main()


