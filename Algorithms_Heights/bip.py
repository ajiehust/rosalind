#!/usr/bin/env python
'''
Testing Bipartiteness
Problem Title: Testing Bipartiteness 
Rosalind Armory ID: BIP
URL: http://rosalind.info/problems/bip/
'''

import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        _t = f.read().strip().split("\n\n")
        n = int(_t[0].strip())
        lst = [l.strip().split("\n") for l in _t[1:]]
        N = [nx.parse_edgelist(l, create_using=nx.Graph(), nodetype=int) for l in lst]
        assert len(N) == n
    return N

def main():
    sys.stdout = open("bip.out", "w")
    print " ".join(map(str, [1 if nx.is_bipartite(G) else -1 for G in fr("bip")]))

if __name__ == '__main__':
    main()
