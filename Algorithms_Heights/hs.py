#!/usr/bin/env python
'''  
Problem Title: Heap Sort 
Rosalind Armory ID: hs
URL: http://rosalind.info/problems/hs/
'''
import sys
import heapq

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip()) 
        lst = map(int, f.readline().strip().split(" "))
        assert len(lst) == n
    return lst

def heapsort(lst):
    result = []
    while lst:
        heapq.heapify(lst)
        result.append(lst[0])
        lst.remove(lst[0])
    return result

def main():
    sys.stdout = open("hs.out", "w")
    print " ".join(map(str, heapsort(fr("hs"))))

if __name__ == '__main__':
    main()
