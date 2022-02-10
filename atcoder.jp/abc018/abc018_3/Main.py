import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import floor, sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from array import array
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
def ceil(a, b): return (a + b - 1) // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    r, c, k = i_map()
    s = s_row_list(r)
    
    sums = [[0] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if s[i][j]=="x":
                sums[i].append(sums[i][-1]+1)
            else:
                sums[i].append(sums[i][-1])

    ans = 0
    for ri in range(k-1,r-k+1):
        for ci in range(k-1,c-k+1):
            for i in range(1,k):
                if sums[ri-i][ci+k-i]!=sums[ri-i][ci-k+1+i]:
                    break
                if sums[ri+i][ci+k-i]!=sums[ri+i][ci-k+1+i]:
                    break
            else:
                if sums[ri][ci+k]==sums[ri][ci-k+1]:
                    ans+=1
    
    print(ans)

if __name__ == '__main__':
    main()
