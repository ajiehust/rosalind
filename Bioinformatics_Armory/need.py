#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Pairwise Global Alignment 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/need/
solution by James Hu@Tue
'''
import sys
from Bio import Entrez, SeqIO, pairwise2
# to make a DNAfull matrix
mtx =[[5,-4,-4,-4,-4,1,1,-4,-4,1,-4,-1,-1,-1,-2,-4],
    [-4,5,-4,-4,-4,1,-4,1,1,-4,-1,-4,-1,-1,-2,5],
    [-4,-4,5,-4,1,-4,1,-4,1,-4,-1,-1,-4,-1,-2,-4],
    [-4,-4,-4,5,1,-4,-4,1,-4,1,-1,-1,-1,-4,-2,-4],
    [-4,-4,1,1,-1,-4,-2,-2,-2,-2,-1,-1,-3,-3,-1,-4],
    [1,1,-4,-4,-4,-1,-2,-2,-2,-2,-3,-3,-1,-1,-1,1],
    [1,-4,1,-4,-2,-2,-1,-4,-2,-2,-3,-1,-3,-1,-1,-4],
    [-4,1,-4,1,-2,-2,-4,-1,-2,-2,-1,-3,-1,-3,-1,1],
    [-4,1,1,-4,-2,-2,-2,-2,-1,-4,-1,-3,-3,-1,-1,1],
    [1,-4,-4,1,-2,-2,-2,-2,-4,-1,-3,-1,-1,-3,-1,-4],
    [-4,-1,-1,-1,-1,-3,-3,-1,-1,-3,-1,-2,-2,-2,-1,-1],
    [-1,-4,-1,-1,-1,-3,-1,-3,-3,-1,-2,-1,-2,-2,-1,-4],
    [-1,-1,-4,-1,-3,-1,-3,-1,-3,-1,-2,-2,-1,-2,-1,-1],
    [-1,-1,-1,-4,-3,-1,-1,-3,-1,-3,-2,-2,-2,-1,-1,-1],
    [-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2],
    [-4,5,-4,-4,-4,1,-4,1,1,-4,-1,-4,-1,-1,-2,5]]
code = ["A","T","G","C","S","W","R","Y","K","M","B","V","H","D","N","U"]
mat = {(code[i],code[j]):mtx[i][j] for i in range(len(code)) for j in range(len(code))}

def main():
    ids = open("need").read().strip().split(" ")
    Entrez.email = "your_name@your_mail_server.com"
    handle = Entrez.efetch(db="nuccore", id=ids, rettype="fasta")
    records = list (SeqIO.parse(handle, "fasta"))
    sys.stdout = open("need.out", "w")
    print int(pairwise2.align.globalds(records[0].seq,records[1].seq, mat,-10,-1, score_only=True))
    #for a in pairwise2.align.globalds(records[0].seq,records[1].seq, mat,-10,-1, score_only=True):
    #    print(pairwise2.format_alignment(*a))

if __name__ == '__main__':
    main()
