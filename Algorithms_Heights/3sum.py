#!/usr/bin/env python
'''
Problem Title: 3SUM
Rosalind Armory ID: 3sum
URL: http://rosalind.info/problems/3sum /
'''
import sys

def fr(fn):
    with open(fn) as f:
        k, _ = map(int, f.readline().strip().split(" ")) 
        lst = [map(int, s.strip().split(" ")) for s in f ]
        assert len(lst) == k
    return lst

def three_sum(lst, k):
    z = sorted(zip(lst, range(len(lst))), key=lambda x:x[0])
    res = []
    for i in range(len(z) - 2):
        if i == 0 or z[i][0] > z[i - 1][0]:
            left = i + 1;right = len(z) - 1
            while left < right:
                if z[left][0] + z[right][0] == -z[i][0]:
                    return sorted([z[i][1] + 1, z[left][1] + 1, z[right][1] + 1])
                    res.append([z[i][1], z[left][1], z[right][1]])
                    left += 1; right -= 1
                    while left < right and z[left][0] == z[left - 1][0]: left += 1
                    while left < right and z[right][0] == z[right + 1][0]: right -= 1
                elif z[left][0] + z[right][0] < -z[i][0]:
                    while left < right:
                        left += 1
                        if z[left][0] > z[left - 1][0]: break
                else:
                    while left < right:
                        right -= 1
                        if z[right][0] < z[right + 1][0]: break
    return [-1]

def main():
    result = [three_sum(lst, 0) for lst in fr("3sum")]
    sys.stdout = open("3sum.out", "w")
    print "\n".join([" ".join(map(str, l)) for l in result ])

if __name__ == '__main__':
    main()
