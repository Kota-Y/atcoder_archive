import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
# from bisect import bisect, bisect_left, bisect_right
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
MOD = 998244353
num_list = []
str_list = []
from operator import mul

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

def main():
    n, K = i_map()
    num_list = i_row_list(n)

    yoko_uf = UnionFind(n)
    tate_uf = UnionFind(n)

    yoko_mem = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = True
            for k in range(n):
                if num_list[i][k] + num_list[j][k] > K:
                    flag = False
                    break
            if flag:
                yoko_uf.unite(i, j)
                yoko_mem = i

    yoko_count = yoko_uf.count(yoko_mem)

    tate_mem = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = True
            for k in range(n):
                if num_list[k][i] + num_list[k][j] > K:
                    flag = False
                    break
            if flag:
                tate_uf.unite(i, j)
                tate_mem = i

    tate_count = tate_uf.count(tate_mem)


    N = 100 + 5
    bikkuri = [0] * N
    bikkuri[0] = 1
    gyaku = [0] * N
    for i in range(1, N):
        bikkuri[i] = (i * bikkuri[i - 1]) % MOD
    gyaku[N - 1] = pow(bikkuri[N - 1], MOD - 2, MOD)
    for i in range(N - 1, 0, -1):
        gyaku[i - 1] = (gyaku[i] * i) % MOD

    ans = 1
    for i in range(n):
        if yoko_uf.findRoot(i) == i:
            ans *= bikkuri[yoko_uf.count(i)]
            ans %= MOD
        if tate_uf.findRoot(i) == i:
            ans *= bikkuri[tate_uf.count(i)]
            ans %= MOD
        yoko_sum = 1
        for i in range(1, yoko_count+1):
            yoko_sum *= i

    print(ans%MOD)

    # tate_sum = 1
    # for i in range(1, tate_count+1):
    #     tate_sum *= i

    # print(yoko_sum * tate_sum%MOD)

if __name__ == '__main__':
    main()
