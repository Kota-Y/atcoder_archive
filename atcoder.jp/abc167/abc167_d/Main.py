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
    n, k = i_map()
    num_list = i_list()

    bin_k = bin(k)[2:]

    len_bin_k = len(bin_k)

    doubling = [[0] * n for i in range(len_bin_k)]

    for i in range(len_bin_k):
        for j in range(n):
            if i == 0:
                doubling[i][j] = num_list[j]
                continue
            doubling[i][j] = doubling[i-1][doubling[i-1][j]-1]

    current_town = 1
    for i, s in enumerate(bin_k):
        if s == '0':
            continue
        current_town = doubling[len_bin_k-i-1][current_town-1]

    print(current_town)

if __name__ == '__main__':
    main()
