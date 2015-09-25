#!/usr/bin/env python
'''
Problem Title: Dijkstra's Algorithm 
Rosalind Armory ID: dij
URL: http://rosalind.info/problems/dij/
'''
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        n, e = map(int, f.readline().strip().split())
        G = nx.parse_edgelist(f.readlines(), create_using=nx.DiGraph(), nodetype=int, data=(('weight', int),))
        assert G.number_of_edges == e
        assert G.number_of_nodes() == n
    return G

def dij(G):
    result = []
    for n in G.nodes():
        if nx.has_path(G, 1, n):result.append(nx.dijkstra_path_length(G, 1, n))
        else: result.append(-1)
    return result

def main():
    sys.stdout = open("dij.out", "w")
    print " ".join(map(str, dij(fr("dij"))))

if __name__ == '__main__':
    main()
