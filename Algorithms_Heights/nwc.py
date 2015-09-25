#!/usr/bin/env python
'''
Problem Title: Negative Weight Cycle
Rosalind Armory ID: nwc
URL: http://rosalind.info/problems/nwc/
'''
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        _t = f.read().strip().split("\n\n")
        n = int(_t[0].strip())
        lst = [l.strip().split("\n") for l in _t[1:]]
        N = [nx.parse_edgelist(l[1:], create_using=nx.DiGraph(), \
                nodetype=int, data=(('weight', int),)) for l in lst]
        assert len(N) == n
    return N

def nwc(G):
    for cyc in list(nx.simple_cycles(G)):
        cyc.append(cyc[0])
        l = 0
        for i in range(len(cyc) - 1):
            l = l + G[cyc[i]][cyc[i + 1]]["weight"]
        if l < 0:
            return 1
    return -1

def main():
    sys.stdout = open("nwc.out", "w")
    print " ".join(map(str, [nwc(G) for G in fr("nwc")]))

if __name__ == '__main__':
    main()
