#!/usr/bin/env python
'''
Problem Title: 3-Way Partition 
Rosalind Armory ID: par3
URL: http://rosalind.info/problems/par3/
'''
import sys

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(" "))  
        assert len(lst) == n
    return lst

def par3(lst):
    # in palace 
    assert len(lst) > 1
    pivot = lst[0]
    i = 1; j = 1
    while j < len(lst):
        if lst[j] == pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        j += 1

    j = len(lst) - 1
    e = i - 1
    while j > i:
        while i < len(lst) and lst[i] < pivot:
            i += 1
        while j > e and lst[j] > pivot:
            j -= 1
        if j > i:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    while lst[i] > pivot:
        i -= 1
    for k in range(e + 1):
        lst[k], lst[i] = lst[i], lst[k]
        i -= 1
    return lst

def main():
    sys.stdout = open("par3.out", "w")
    print " ".join(map(str, par3(fr("par3"))))

if __name__ == '__main__':
    main()
