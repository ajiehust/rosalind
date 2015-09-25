#!/usr/bin/env python
'''
Problem Title: M2SUM 
Rosalind Armory ID: 2sum
URL: http://rosalind.info/problems/2sum /
'''
import sys
from collections import defaultdict

def fr(fn):
    with open(fn) as f:
        k, _ = map(int, f.readline().strip().split(" ")) 
        lst = [map(int, s.strip().split(" ")) for s in f ]
        assert len(lst) == k
    return lst

def two_sum(lst, k):
    # hash then return
    elmt_hash = defaultdict(set)
    for idx, elm in enumerate(lst):
        elmt_hash[elm].add(idx)
    # loop over all elem in the hash
    for e in elmt_hash:
        if k - e == e and len(elmt_hash[e]) > 1:
            return sorted([elmt_hash[e].pop() + 1, elmt_hash[e].pop() + 1]) 
        if k - e != e and -e in elmt_hash:
            return sorted([elmt_hash[e].pop() + 1, elmt_hash[k - e].pop() + 1])
    return [-1]

def main():
    result = [two_sum(lst, 0) for lst in fr("2sum")]
    sys.stdout = open("2sum.out", "w")
    print "\n".join([" ".join(map(str, l)) for l in result ])

if __name__ == '__main__':
    main()
