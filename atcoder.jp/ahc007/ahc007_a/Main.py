import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import ceil, floor, sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

class UnionFind:
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rank = [0]*(n+1)

    # ノードxのrootノードを見つける
    def findRoot(self, x):
        if(self.root[x] < 0): # 根
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.findRoot(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.findRoot(x)
        y = self.findRoot(y)

        # すでに同じ木に属していた場合
        if x == y:
            return 

        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

    # ノードxが属する木のサイズを返す
    def count(self, x):
        return -self.root[self.findRoot(x)]

    # グループ数をカウント
    def groupCount(self):
        count = 0
        for i in range(1, self.n+1):
            if self.root[i] < 0: 
                count += 1
        return count

def dist(x0, y0, x1, y1):
    return round(pow(pow(x0-x1, 2) + pow(y0-y1, 2) , 0.5))

def main():
    n = 400
    m = 1995
    n_list = i_row_list(n)
    m_list = i_row_list(m)

    edge_list = []
    for i, (u, v) in enumerate(m_list):
        x0, y0 = n_list[u][0], n_list[u][1]
        x1, y1 = n_list[v][0], n_list[v][1]
        l = dist(x0, y0, x1, y1)
        edge_list.append((l, u, v, i))

    edge_list.sort()

    ans_list = [0] * m

    uf = UnionFind(n)
    for l, u, v, i in edge_list:
        if uf.isSameGroup(u, v):
            continue
        uf.unite(u, v)
        ans_list[i] = 1

    edge_list_l_sort = deepcopy(edge_list)
    
    edge_list_i_sort = sorted(edge_list, key=lambda x: x[3])
    
    sw_count = 0

    for i in range(m):
        input_l = i_input()
        if sw_count <= 3 and ans_list[i] == 1 and edge_list_i_sort[i][0] * 2.5 <= input_l:
            sw_count += 1
            uf = UnionFind(n)

            for k in range(i):
                if ans_list[k] == 1:
                    a = edge_list_i_sort[k][1]
                    b = edge_list_i_sort[k][2]
                    uf.unite(a, b)

            ans_list_tmp = [0] * m
            for l, u, v, j in edge_list_l_sort:
                if i == j:
                    continue
                if uf.isSameGroup(u, v):
                    continue
                uf.unite(u, v)
                ans_list_tmp[j] = 1

            if uf.groupCount() <= 1:
                ans_list = ans_list_tmp

        print(ans_list[i])
        sys.stdout.flush()

if __name__ == '__main__':
    main()
