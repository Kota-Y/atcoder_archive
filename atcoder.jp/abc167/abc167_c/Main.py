import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
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

def main():
    n, m, x = i_map()
    num_list = i_row_list(n)

    money = INF

    for bit in list(product([0,1], repeat=n)):
        tmp_money = 0
        alg_list = [0] * m
        for i in range(n):
            if bit[i] == 1:
                tmp_money += num_list[i][0]
                for j in range(m):
                    alg_list[j] += num_list[i][j+1]
        for i in range(m):
            if alg_list[i] < x:
                tmp_money = INF
                break
        money = min(money, tmp_money)

    print(money if money != INF else -1)

if __name__ == '__main__':
    main()
