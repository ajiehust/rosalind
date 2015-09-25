#!/usr/bin/env python
'''
Problem Title: Median 
Rosalind Armory ID: med
URL: http://rosalind.info/problems/med/
'''
import sys, heapq

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip()) 
        lst = map(int, f.readline().strip().split(" "))
        k = int(f.readline().strip())
    return n, lst, k

def med(n, lst, k):
    assert n == len(lst)
    assert n > k
    l = lst[0:k]
    heapq._heapify_max(l)
    for i in range(k, n):
        if lst[i] < l[0]:
            heapq._heappushpop_max(l, lst[i])
    return l[0]

def main():
    sys.stdout = open("med.out", "w")
    print  med(*fr("med"))

if __name__ == '__main__':
    main()
