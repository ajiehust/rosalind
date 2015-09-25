#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Problem Title: Fibonacci Numbers 
Rosalind/Algorithms Heights
URL: http://rosalind.info/problems/fibo/
solution by James Hu@Tue
'''
import sys

def fibo(n):
    if n <= 2 : return 1
    else: return fibo(n-2) + fibo(n -1) 

def main():
    with open("fibo") as f:
        n = int(f.readline().strip())
        sys.stdout = open("fibo.out","w")
        print fibo(n)

if __name__ == '__main__':
    main()
