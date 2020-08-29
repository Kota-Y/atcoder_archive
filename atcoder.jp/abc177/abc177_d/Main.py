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

def main():
    n, m = i_map()

    uf = UnionFind(n)

    for _ in range(m):
        a, b = i_map()
        
        if uf.isSameGroup(a, b):
            continue
        else:
            uf.unite(a, b)

    max_count = 0
    for i in range(n):
        max_count = max(max_count, uf.count(i))

    print(max_count)

if __name__ == '__main__':
    main()
