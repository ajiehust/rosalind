#!/usr/bin/env python
'''
Double-Degree Array 
Problem Title: Double-Degree Array 
Rosalind Armory ID: ddeg
URL: http://rosalind.info/problems/ddeg/
'''
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        lines = f.readlines()
        n, e = map(int, lines[0].strip().split(" "))
        G = nx.parse_edgelist(lines[1:], create_using=nx.Graph(), nodetype=int)
        [G.add_node(i) for i in set(range(1, n + 1)) - set(G.nodes())]
        assert len(G.edges()) == e
    return G

def ddeg(G):
    return [sum(map(lambda x:nx.degree(G, x), nx.neighbors(G, n))) for n in G.nodes()]

def main():
    sys.stdout = open("ddeg.out", "w")
    print " ".join(map(str, ddeg(fr("ddeg"))))

if __name__ == '__main__':
    main()

