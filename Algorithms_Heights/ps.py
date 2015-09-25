#!/usr/bin/env python
'''
Partial Sort 
Rosalind Armory ID: ps
URL: http://rosalind.info/problems/ps/
'''
import sys, random

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip()) 
        lst = map(int, f.readline().strip().split(" "))
        k = int(f.readline().strip())
        assert len(lst) == n
    return lst, k

def ps(lst, k):
    if len(lst) == k: return lst
    pivot = lst[random.randrange(len(lst))]
    lst1, lst2 = [], []
    for i in lst:
        if i <= pivot: lst1.append(i)
        else: lst2.append(i)
    if len(lst1) >= k: return ps(lst1, k)
    else: return lst1 + ps(lst2, k - len(lst1))

def main():
    sys.stdout = open("ps.out", "w")
    print " ".join(map(str, ps(*fr("ps"))))

if __name__ == '__main__':
    main()
