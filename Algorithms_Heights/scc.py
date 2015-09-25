#!/usr/bin/env python
'''
Problem Title: Strongly Connected Components
Rosalind Armory ID: scc
URL: http://rosalind.info/problems/scc/
# result is always wrong
'''
import sys
import networkx as nx

def fr(f):
    t = open(f).readlines()
    _, e = map(int, t[0].strip().split(" "))
    G = nx.parse_edgelist(t[1:], create_using=nx.DiGraph(), nodetype=int)
    assert len(G.edges()) == e
    return G

def scc(G):
    return nx.number_strongly_connected_components(G)

def main():
    sys.stdout = open("scc.out", "w")
    print scc(fr("scc"))

if __name__ == '__main__':
    main()
