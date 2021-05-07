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

def changeIntToStr(r, c):
    if len(str(c)) != 4:
        sc = '0' * (4 - len(str(c))) + str(c)
        rc = int(str(r)+sc)
    else:
        rc = int(str(r)+str(c))       
    return rc

def printMapList(map_list,h):
    for i in range(h):
        print(*map_list[i])

def main():
    h, w = i_map()
    q = i_input()

    uf = UnionFind(20002001)

    map_list = [[0] * w for i in range(h)]

    for _ in range(q):
        tmp = i_list()
        if tmp[0] == 1:
            r, c = tmp[1], tmp[2]
            map_list[r-1][c-1] = 1
            rc = changeIntToStr(r, c)
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                ni = r-1 + dx
                nj = c-1 + dy
                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    continue
                if map_list[ni][nj] == 0:
                    continue
                nrc = changeIntToStr(ni+1, nj+1)
                uf.unite(rc, nrc)
                # print('1!!!',r-1,c-1, ni,nj,rc,nrc)
            # printMapList(map_list,h)
        else:
            ra, ca, rb, cb = tmp[1], tmp[2], tmp[3], tmp[4]
            arc = changeIntToStr(ra, ca)
            brc = changeIntToStr(rb, cb)
            # print('2!!!',arc,brc)
            if uf.isSameGroup(arc, brc) and map_list[ra-1][ca-1] == 1 and map_list[rb-1][cb-1]:
                print('Yes')
            else:
                print('No')
    
if __name__ == '__main__':
    main()
