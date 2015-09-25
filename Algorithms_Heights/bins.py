#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Binary Search 
Rosalind/Algorithms Heights
URL: http://rosalind.info/problems/bins/
solution by James Hu@Tue
'''
import sys

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())
        lst1 = map(int, f.readline().strip().split(" "))
        lst2 = map(int, f.readline().strip().split(" "))
    assert len(lst1) == n
    assert len(lst2) == m
    return lst1, lst2

def bins(n, lst, l, r):
    if l > r:
        return -1
    else:
        mid = (l + r) / 2
        if n == lst[mid]:
            return mid + 1
        elif n < lst[mid]:
            return bins(n, lst, l, mid - 1)
        else:
            return bins(n, lst, mid + 1, r)

def main():
    lst1, lst2 = fr("bins")
    sys.stdout = open("bins.out","w")
    print " ".join(map(str, [bins(n, lst1, 0, len(lst1)) for n in lst2]))

if __name__ == '__main__':
    main()

