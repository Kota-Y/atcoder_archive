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
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

# ダイクストラ法(始点sから各頂点への最短距離)、オーダー: MlogN, N:ノード数, M:エッジ数
#d:各頂点へのコスト(存在しないときはinf)
#q:キュー(スタートからのコスト,頂点)
def dijkstra(start: int, node_num: int, edge: list) -> list:
    d = [float("inf")] * node_num
    d[start] = 0
    #スタートをキューに入れる
    q = [(0,start)]

    while len(q) != 0:
        #キューの先頭を取得
        ci, i = heappop(q)
        if d[i] < ci:
            continue
        #キューの先頭から繋がっている頂点を探索
        for cj, j in edge[i]:
            if d[j] > d[i] + cj:
                d[j] = d[i] + cj
                heappush(q, (d[j], j))
    return d

def main():
    n, m, t = i_map()
    money_list = i_list()

    go_edge = [[] for _ in range(n)]
    back_edge = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = i_map()
        go_edge[a-1].append((c, b-1))
        back_edge[b-1].append((c, a-1))

    go = dijkstra(0, n, go_edge)
    back = dijkstra(0, n, back_edge)

    ans = 0
    for v in range(n):
        stay_time = t - (go[v] + back[v])
        ans = max(ans, stay_time * money_list[v])

    print(ans)

if __name__ == '__main__':
    main()
