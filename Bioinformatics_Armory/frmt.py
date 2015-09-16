#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Data Formats 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/frmt/
solution by James Hu@Tue
'''
from Bio import Entrez, SeqIO

def main():
    with open("frmt") as f:
        ids = f.readline().strip().split(" ")
        Entrez.email = "your_name@your_mail_server.com"
        handle = Entrez.efetch(db="nuccore", id=ids, rettype="fasta")
        records = list (SeqIO.parse(handle, "fasta"))
        records = sorted(records, key=lambda s:len(s.seq))
        SeqIO.write(records[0], open("frmt.out", "w"), "fasta")

if __name__ == '__main__':
    main()
