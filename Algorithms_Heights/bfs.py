#!/usr/bin/env python
'''
Breadth-First Search
Problem Title: Breadth-First Search  
Rosalind Armory ID: bfs
URL: http://rosalind.info/problems/bfs/

'''
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        n, e = map(int, f.readline().strip().split(" "))
        G = nx.parse_edgelist(f.readlines(), create_using=nx.DiGraph(), nodetype=int)
        assert G.number_of_nodes() == n
        assert G.number_of_edges() == e
    return G

def bfs(G):
    length = nx.single_source_shortest_path_length(G, 1)
    return [length.get(v,-1) for v in G.nodes()]
    
def main():
    sys.stdout = open("bfs.out","w")
    print " ".join(map(str, bfs(fr("bfs"))))
    
if __name__ == '__main__':
    main()
