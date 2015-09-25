#!/usr/bin/env python
'''
Problem Title: Testing Acyclicity
Rosalind Armory ID: dag
URL: http://rosalind.info/problems/dag/
'''
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        _t = f.read().strip().split("\n\n")
        n = int(_t[0].strip())
        lst = [l.strip().split("\n") for l in _t[1:]]
        N = [nx.parse_edgelist(l, create_using=nx.DiGraph(), nodetype=int) for l in lst]
        assert len(N) == n
    return N

def dag(G):
    return nx.is_directed_acyclic_graph(G)

def main():
    sys.stdout = open("dag.out", "w")
    print " ".join(["1" if nx.is_directed_acyclic_graph(G) else "-1" for G in fr("dag")])

if __name__ == '__main__':
    main()
