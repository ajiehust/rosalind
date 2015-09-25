#!/usr/bin/env python
'''
Problem Title: Bellman-Ford Algorithm 
Rosalind Armory ID: bf
URL: http://rosalind.info/problems/bf/
'''
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        f.readline()
        G = nx.parse_edgelist(f.readlines(), create_using=nx.DiGraph(), nodetype=int, data=(('weight', int),))
    return G

def bf(G):
    bf = nx.bellman_ford(G, 1)[1]
    return [bf.get(n, "x") for n in sorted(G.nodes())]

def main():
    sys.stdout = open("sdag.out", "w")
    print " ".join(map(str, bf(fr("sdag"))))

if __name__ == '__main__':
    main()
