#!/usr/bin/env python
'''
Problem Title: General Sink
Rosalind Armory ID: gs
URL: http://rosalind.info/problems/gs/
'''
import sys
import networkx as nx

def fr(f):
    with open(f) as f:
        t = f.read().strip().split("\n\n")
        n = int(t[0])
        lines = [x.split("\n")[1:] for x in t[1:]]
        N = [nx.parse_edgelist(l, create_using=nx.DiGraph(), nodetype=int) for l in lines ]
        assert len(N) == n
        return N

def gs(N):
    result = []
    for G in N:
        nodes = G.nodes()
        for v in nodes:
            marker = True
            for t in nodes:
                if v != t: 
                    if not nx.has_path(G, v, t):
                        marker = False;break
            if marker:result.append(v);break
        if not marker:result.append(-1)
    return result

def main():
    sys.stdout = open("gs.out","w")
    print " ".join(map(str, gs(fr("gs"))))

if __name__ == '__main__':
    main()
