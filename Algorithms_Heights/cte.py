#!/usr/bin/env python
'''
Problem Title: Shortest Cycle Through a Given Edge
Rosalind Armory ID: cte
URL: http://rosalind.info/problems/cte/
'''
import sys, re
import networkx as nx

def fr(f):
    with open(f) as f:
        lst = re.split("\n\d+ \d+\n", f.read())
        lst = [l.strip().split("\n") for l in lst[1:]]
        first_edges = [map(int, l[0].split(" "))[:2] for l in lst]
        N = [nx.parse_edgelist(l, create_using=nx.DiGraph(), nodetype=int, \
                               data=(('weight', int),)) for l in lst]
        return N, first_edges

def cte(N, first_edges):
    result = []
    for G, edge in zip(N, first_edges):
        v, t = edge
        l_vt = G[v][t]["weight"]
        G.remove_edge(v, t)
        if nx.has_path(G, t, v):
            # must use this method otherwise wrong 
            # nx.shortest_path_length(G, t, v, weight="weight") not work
            shortest_tv = nx.dijkstra_path_length(G, t, v)
            result.append(l_vt + shortest_tv)
        else:
            result.append(-1)
    return result
    
def main():
    sys.stdout = open("cte.out", "w")
    print " ".join(map(str, cte(*fr("cte"))))

if __name__ == '__main__':
    main()
