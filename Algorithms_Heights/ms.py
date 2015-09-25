#!/usr/bin/env python
'''
Merge Sort 
Problem Title: Merge Sort 
Rosalind Armory ID: ms
URL: http://rosalind.info/problems/ms/
'''
import sys

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(" "))  
        assert len(lst) == n
    return lst

def mer(lst1, lst2):
    result = []
    while lst1 and lst2:
        result.append(lst1.pop(0) if lst1[0] <= lst2[0] else lst2.pop(0))
    return result + lst1 + lst2

def ms(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) / 2 
    lst1 = ms(lst[:mid])
    lst2 = ms(lst[mid:])
    return mer(lst1, lst2)

def main():
    sys.stdout = open("ms.out", "w")
    print " ".join(map(str, ms(fr("ms"))))

if __name__ == '__main__':
    main()
