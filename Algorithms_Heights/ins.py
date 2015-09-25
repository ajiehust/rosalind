#!/usr/bin/env python
'''
Insertion Sort 
Problem Title: Insertion Sort 
Rosalind Armory ID: ins
URL: http://rosalind.info/problems/ins/
'''
import sys

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(" "))
        assert len(lst) == n
    return lst

def ins(lst):
    count = 0
    for i in range(1, len(lst)):
        k = i
        while k > 0 and lst[k] < lst[k - 1]:
            tmp = lst[k]
            lst[k] = lst[k - 1]
            lst[k - 1] = tmp
            count += 1
            k -= 1
    return count
    
def main():
    sys.stdout = open("ins.out", "w")
    print ins(fr("ins"))

if __name__ == '__main__':
    main()
