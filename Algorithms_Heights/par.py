#!/usr/bin/env python
'''
Problem Title:2-Way Partition  
Rosalind Armory ID: par
URL: http://rosalind.info/problems/par/
'''
import sys

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(" "))
        assert len(lst) == n
    return lst

def par(lst):
    # inpalace 
    assert len(lst) > 1
    pivot = lst[0]
    l = 1 
    r = len(lst) - 1
    while r > l:
        while l <= len(lst) - 1 and lst[l] <= pivot:
            l += 1
        while r > 0 and lst[r] > pivot:
            r -= 1
        if r > l:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
    lst[0], lst[l - 1] = lst[l - 1], lst[0]
    return lst

def main():
    sys.stdout = open("par.out", "w")
    print " ".join(map(str, par(fr("par"))))

if __name__ == '__main__':
    main()
