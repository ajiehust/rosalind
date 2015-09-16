#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: FASTQ format introduction 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/tfsq/
solution by James Hu@Tue
'''

from Bio import SeqIO
def main():
    SeqIO.convert("tfsq", "fastq", "tfsq.out", "fasta")
    
if __name__ == '__main__':
    main()
