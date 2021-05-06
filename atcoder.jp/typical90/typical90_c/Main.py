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

def bfs(graph: list, n: int, start: int, ans: list):
    q = deque([start])
    visited = [INF] * n
    visited[start] = 1
    while len(q) != 0:
        node = q.popleft()
        for leaf in graph[node]:
            if visited[leaf] != INF:
                continue
            ans[leaf] = ans[node] + 1
            visited[leaf] = 1
            q.append(leaf)

def main():
    n = i_input()
    num_list = i_row_list(n-1)

    graph = create_graph(n, num_list)

    ans_list = [0] * n
    bfs(graph, n, 1, ans_list)

    max_num = max(ans_list)
    max_index = ans_list.index(max_num)

    ans_list = [0] * n
    bfs(graph, n, max_index, ans_list)

    print(max(ans_list)+1)

if __name__ == '__main__':
    main()
