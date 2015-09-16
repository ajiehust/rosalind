#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Read Filtration by Quality 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/filt/
solution by James Hu@Tue
'''
import sys, numpy
from Bio import SeqIO

def main():
    with open("filt") as f:
        threshold, percent = map(int, f.readline().strip().split(" "))
        fastq = list (SeqIO.parse(f, "fastq"))
        fastx = numpy.array([rcd.letter_annotations["phred_quality"] for rcd in fastq])
        fastx = numpy.array([len(rcd[rcd >= threshold]) * 100 / len(rcd) for rcd in fastx])
        sys.stdout = open("filt.out", "w")
        print len(fastx[fastx >= percent])

if __name__ == '__main__':
    main()
