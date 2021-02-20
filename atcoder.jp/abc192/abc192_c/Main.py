import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def g1(x):
    tmp = [int(c) for c in str(x)]
    tmp.sort(reverse=True)
    ans = 0
    for i in range(len(tmp)):
        ans += pow(10, (len(tmp)-i-1)) * tmp[i]
    return ans

def g2(x):
    tmp = [int(c) for c in str(x)]
    tmp.sort()
    ans = 0
    for i in range(len(tmp)):
        ans += pow(10, (len(tmp)-i-1)) * tmp[i]
    return ans

def main():
    n, k = i_map()
    
    if k == 0:
        print(n)
        exit()

    for i in range(k):
        n = g1(n) - g2(n)

    print(n)

if __name__ == '__main__':
    main()
