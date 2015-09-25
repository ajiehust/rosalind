#!/usr/bin/env python
'''
Majority Element
Problem Title: Majority Element
Rosalind Armory ID: maj
URL: http://rosalind.info/problems/maj/
'''
import sys

def fr(fn):
    with open(fn) as f:
        k, _n = map(int, f.readline().strip().split(" "))
        lst = [map(int, l.strip().split(" ")) for l in f]
        assert len(lst) == k
    return lst

def maj(lst):
    max_freq = max(set(lst), key=lst.count)
    if lst.count(max_freq) > len(lst) / 2: return max_freq
    else: return -1

def main():
    sys.stdout = open("maj.out", "w")
    print " ".join(map(str, [maj(lst) for lst in fr("maj")]))

if __name__ == '__main__':
    main()
