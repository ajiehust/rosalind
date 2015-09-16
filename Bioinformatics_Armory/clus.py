#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Global Multiple Alignment 
Rosalind/Bioinformatics Armory
URL: http://rosalind.info/problems/clus/
solution by James Hu@Tue
'''
from subprocess import call

def main():
    call("clustalo -i clus -o clus.out -v", shell=True)
    print open("clus.out").read()
if __name__ == '__main__':
    main()
