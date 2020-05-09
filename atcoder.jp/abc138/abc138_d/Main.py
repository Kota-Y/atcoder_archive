import sys, re
from math import ceil, floor, sqrt, pi#, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_rpw_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_list(N): return [s_list() for _ in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7

def dfs(current, parent, edges, ans_list):
    for child in edges[current]:
        if child == parent:
            continue
        ans_list[child] += ans_list[current]
        dfs(child, current, edges, ans_list)

def main():
    n, q = i_map()

    edges = [[] for _ in range(n)]
    for i in range(n-1):
        a, b = i_map()
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)

    ans_list = [0] * n
    for i in range(q):
        p, x = i_map()
        ans_list[p-1] += x

    dfs(0, -1, edges, ans_list)

    print(*ans_list)

if __name__ == '__main__':
    main()