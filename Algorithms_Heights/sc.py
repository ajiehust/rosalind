#!/usr/bin/env python
'''
Problem Title: Semi-Connected Graph
Rosalind Armory ID: sc
URL: http://rosalind.info/problems/sc/
'''
import sys
import networkx as nx

def fr(f):
    with open(f) as f:
        t = f.read().strip().split("\n\n")
        n = int(t[0])
        N = [nx.parse_edgelist(l, create_using=nx.DiGraph(), nodetype=int) \
             for l in [x.split("\n")[1:] for x in t[1:]] ]
        assert len(N) == n
        return N

def sc(N):
    return [1 if nx.is_semiconnected(G) else -1 for G in N ]

def main():
    sys.stdout = open("sc.out","w")
    print " ".join(map(str, sc(fr("sc"))))

if __name__ == '__main__':
    main()
