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

def create_graph(n: int, l: list) -> list:
    graph = [[] for _ in range(n)]
    for a, b in l:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return graph

def dfs(edges, color_list, current_color, position):
    color_list[position] = current_color
    for child in edges[position]:
        if color_list[child] == -1:     
            dfs(edges, color_list, 1-current_color, child)

def main():
    n = i_input()
    num_list = i_row_list(n-1)

    edge_list = create_graph(n, num_list)
    color_list = [-1] * n

    dfs(edge_list, color_list, 0, 0)

    zero_count = color_list.count(0)
    ans_list = []
    if zero_count >= n // 2:
        count = 0
        for i in range(n):
            if count == n // 2:
                break
            if color_list[i] == 0:
                ans_list.append(i+1)
                count += 1
    else:
        count = 0
        for i in range(n):
            if count == n // 2:
                break
            if color_list[i] == 1:
                ans_list.append(i+1)
                count += 1

    print(*ans_list)

if __name__ == '__main__':
    main()
