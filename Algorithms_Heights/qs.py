#!/usr/bin/env python
'''
Problem Title: Quick Sort 
Rosalind Armory ID: qs
URL: http://rosalind.info/problems/qs/
'''
import sys, random

def fr(f):
    n, lst = open(f).readlines()
    n = int(n);lst = map(int, lst.strip().split(" "))
    assert len(lst) == n
    return lst

def qs(lst):
    if len(lst) <= 1: return lst
    p = lst[random.randint(0, len(lst) - 1)]  # randomly select one item
    l, e, g = [], [], []
    for x in lst:
        if x < p:l.append(x)
        elif x == p:e.append(x)
        else: g.append(x)
    return qs(l) + e + qs(g)

def main():
    sys.stdout = open("qs.out", "w")
    print " ".join(map(str, qs(fr("qs"))))

if __name__ == '__main__':
    main()
