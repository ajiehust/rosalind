#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Degree Array 
Rosalind/Algorithms Heights
URL: http://rosalind.info/problems/deg/
solution by James Hu@Tue
'''

import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        lines = f.readlines()
        n, e = map(int, lines[0].strip().split(" "))
        G = nx.parse_edgelist(lines[1:], create_using=nx.Graph(), nodetype=int)
        assert len(G.nodes()) == n
        assert len(G.edges()) == e
    return G

def deg(G):
    return [len(nx.neighbors(G, n)) for n in G.nodes()]

def main():
    sys.stdout = open("deg.out", "w")
    print deg(fr("deg"))

if __name__ == '__main__':
    main()
