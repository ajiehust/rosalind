#!/usr/bin/env python
'''
Connected Components 
Problem Title: Connected Components  
Rosalind Armory ID: cc
URL: http://rosalind.info/problems/cc/
'''
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        _n, e = map(int, f.readline().strip().split(" "))
        G = nx.parse_edgelist(f.readlines(), create_using=nx.Graph(), nodetype=int)
        assert G.number_of_edges() == e
    return G

def cc(G):
    return nx.number_connected_components(G)

def main():
    sys.stdout = open("cc.out", "w")
    print cc(fr("cc"))

if __name__ == '__main__':
    main()
