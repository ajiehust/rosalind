#!/usr/bin/env python
'''
Problem Title: Topological Sortingh 
Rosalind Armory ID: ts
URL: http://rosalind.info/problems/ts/
'''
import sys
import networkx as nx

def fr(f):
    with open(f) as f:
        n = int(f.readline().strip())
        lst = []
        for _ in range(n):
            _l = []
            n, e = map(int, f.readline().strip().split(" "))
            for __ in range(e):
                _l.append(f.readline().strip())
            lst.append(_l)
        return [nx.parse_edgelist(l, create_using=nx.DiGraph(), nodetype=int) for l in lst]

def hdag(N):
    for G in N:
        lst = list(nx.dfs_postorder_nodes(G))[::-1]
        mk = True
        for v in lst[:-1]:
            if not nx.has_path(G, v, lst[lst.index(v) + 1]):  # much faster
                print -1
                mk = False
                break
        if mk: print 1, " ".join(map(str, lst))

def main():
    sys.stdout = open("hdag.out", "w")
    hdag(fr("hdag"))

if __name__ == '__main__':
    main()
