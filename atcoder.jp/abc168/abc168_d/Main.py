import sys, re
from math import ceil, floor, sqrt, pi, factorial#, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def bfs(graph: list, n: int, start: int, ans: list):
    q = deque([start])
    visited = [INF] * n
    visited[0] = 1
    while len(q) != 0:
        node = q.popleft()
        for leaf in graph[node]:
            if visited[leaf] != INF:
                continue
            ans[leaf] = node + 1
            visited[leaf] = 1
            q.append(leaf)

def create_graph(n: int, l: list) -> list:
    graph = [[] for _ in range(n)]
    for a, b in l:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    return graph

def main():
    n, m = i_map()
    num_list = i_row_list(m)

    graph = create_graph(n, num_list)

    ans = [0] * n

    bfs(graph, n, 0, ans)

    Yes()
    for a in ans[1:]:
        print(a)

if __name__ == '__main__':
    main()
