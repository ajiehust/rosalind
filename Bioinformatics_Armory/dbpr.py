#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Introduction to Protein Databases 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/dbpr/
solution by James Hu@Tue
'''
import sys
from Bio import ExPASy, SwissProt

def main():
    with open("dbpr") as f:
        handle = ExPASy.get_sprot_raw(f.readline().strip())
        record = SwissProt.read(handle)
        record = [x[2] for x in record.cross_references if x[0] == 'GO']
        record = [x[2:] for x in record if x[0] == 'P']
        sys.stdout = open("dbpr.out","w")
        print "\n".join(record)

if __name__ == '__main__':
    main()