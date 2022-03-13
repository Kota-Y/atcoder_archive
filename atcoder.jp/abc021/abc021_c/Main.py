import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
def floor(a, b): return a // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    n = i_input()
    a, b = i_map()
    m = i_input()

    graph = [[] for i in range(n)]
    for i in range(m):
        x,y = i_map()
        graph[x-1].append(y-1)
        graph[y-1].append(x-1) 

    visited = [INF for _ in range(n)]
    visited[a-1] = 0
    count = [0 for i in range(n)]
    count[a-1] = 1
    que = deque()
    que.append(a-1)

    while que:
        j = que.popleft()
        for i in graph[j]:
            if visited[j] + 1 <= visited[i]:
                count[i] += count[j]
                if visited[i] == INF:
                    visited[i] = visited[j] + 1
                    que.append(i)

    print(count[b-1] % MOD)

if __name__ == '__main__':
    main()
