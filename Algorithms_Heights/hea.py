#!/usr/bin/env python
'''
Building a Heap  
Problem Title: Building a Heap 
Rosalind Armory ID: hea
URL: http://rosalind.info/problems/hea/
'''
import sys
import heapq

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(" "))
        assert len(lst) == n
    return lst

def hea(lst):
    heapq._heapify_max(lst)
    return lst

def main():
    sys.stdout = open("hea.out","w")
    print " ".join(map(str, hea(fr("hea"))))

if __name__ == '__main__':
    main()
