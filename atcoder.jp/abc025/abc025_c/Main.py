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

b = i_row_list(2)
c = i_row_list(3)

s = 0
for i in b:
    s += sum(i)
for i in c:
    s += sum(i)

def score(g):
    count = 0
    for i in range(3):
        for j in range(3):
            if i < 2:
                if g[i*3+j] == g[(i+1)*3+j]:
                    count += b[i][j]
                else:
                    count -= b[i][j]
            if j < 2:
                if g[i*3+j] == g[i*3+j+1]:
                    count += c[i][j]
                else:
                    count -= c[i][j]
    return count
 
def dfs(x,done):
    if -1 not in done:
        s = score(done)
        
        return s
 
    cand = []
    for i in range(3):
        for j in range(3):
            if done[i*3+j] == -1:
                t = done[:i*3+j]+[x%2]+done[i*3+j+1:]
                cand.append(dfs(x+1,t))
    if x%2 == 0:
        ans = max(cand)
    else:
        ans = min(cand)
    
    return ans

a = dfs(0, [-1] * 9)

print((s+a)//2)
print((s-a)//2)
