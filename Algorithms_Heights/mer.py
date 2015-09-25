#!/usr/bin/env python
'''
Merge Two Sorted Arrays
Problem Title: Merge Two Sorted Arrays
Rosalind Armory ID: mer
URL: http://rosalind.info/problems/mer/
'''
import sys

def fr(fn):
    with open("mer") as f:
        n = int(f.readline().strip())
        lst1 = map(int, f.readline().strip().split())
        assert len(lst1) == n
        n = int(f.readline().strip())
        lst2 = map(int, f.readline().strip().split())
        assert len(lst2) == n
    return lst1, lst2

def mer(lst1, lst2):
    result = []
    while lst1 and lst2:
        if lst1[0] <= lst2 [0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))
    return result + lst1 + lst2

def main():
    sys.stdout = open("mer.out","w")
    print " ".join(map(str, mer(*fr("mer"))))

if __name__ == '__main__':
    main()
