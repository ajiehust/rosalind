#!/usr/bin/env python
'''
Problem Title: Square in a Graph 
Rosalind Armory ID: sq
URL: http://rosalind.info/problems/sq/
'''
import sys
import networkx as nx

def fr(f):
    with open(f) as f:
        t = f.read().strip().split("\n\n")
        n = int(t[0])
        lines = [x.split("\n")[1:] for x in t[1:]]
        N = [nx.parse_edgelist(l, nodetype=int) for l in lines ]
        assert len(N) == n
        return N

def helper(G, n, l, seen):
    if l == 3:
        if seen[0] in G.neighbors(n):
            return 1
        else:
            return 0
    else:
        if len(set(G.neighbors(n)) - set(seen)) == 0:
            return 0
        else:
            return sum([helper(G, m, l + 1, seen + [m]) for m in G.neighbors(n) if m not in seen])

def sq(G):
    for n in G.nodes():
        if helper(G, n, 0, [n]) >= 1:return 1
    return -1

def main():
    sys.stdout = open("sq.out", "w")
    print " ".join(map(str, [sq(G) for G in fr("sq")]))

if __name__ == '__main__':
    main()
