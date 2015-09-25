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
        l = f.read().strip().split("\n")[1:]
        G = nx.parse_edgelist(l, create_using=nx.DiGraph(), nodetype=int)
        return G

def ts(G):
    return nx.topological_sort_recursive(G)

def main():
    sys.stdout = open("ts.out", "w")
    print " ".join(map(str, ts(fr("ts"))))

if __name__ == '__main__':
    main()
