#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Base Filtration by Quality 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/bfil/
solution by James Hu@Tue
'''
import sys
import numpy as np
from Bio import SeqIO

def trim(lst, threshold):
    res = []
    for i in xrange(len(lst)):
        if lst[i] >= threshold:
            res.append(i)
            break
    for j in range(len(lst))[::-1]:
        if lst[j] >= threshold:
            res.append(j)
            break
    return res

def main():
    with open("bfil") as f:
        threshold = int(f.readline().strip())
        records = list(SeqIO.parse(f, "fastq"))
        fastq = np.array([rcd.letter_annotations["phred_quality"] for rcd in records])
        trim_idx = [trim(fq, threshold) for fq in fastq]
        trimed_fastq = [fq[idx[0]:idx[1] + 1] for fq, idx in zip(records, trim_idx)]
        sys.stdout = open("bfil.out", "w")
        print "".join([fq.format("fastq") for fq in trimed_fastq])

if __name__ == "__main__":
    main()
