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

def main():
    n, m = i_map()
    h_list = i_list()
    w_list = i_list()

    h_list.sort()
    w_list.sort()

    gusu_list = [0]
    kisu_list = [0]

    for i in range(n):
        if i % 2 == 0:
            gusu_list.append(gusu_list[i//2]+h_list[i])
        else:
            kisu_list.append(kisu_list[i//2]+h_list[i])

    min_sum = INF

    for w in w_list:
        gusu_count = 0
        kisu_count = 0

        insert_index = bisect_left(h_list, w)

        if insert_index % 2 == 0:
            gusu_count = gusu_list[insert_index//2] + w + (kisu_list[n//2] - kisu_list[insert_index//2])
            kisu_count = kisu_list[insert_index//2] + (gusu_list[n//2+1] - gusu_list[insert_index//2])
        else:
            gusu_count = gusu_list[insert_index//2+1] + (kisu_list[n//2] - kisu_list[insert_index//2])
            kisu_count = kisu_list[insert_index//2] + w + (gusu_list[n//2+1] - gusu_list[insert_index//2+1])

        min_sum = min(min_sum, abs(gusu_count - kisu_count))

    print(min_sum)

if __name__ == '__main__':
    main()
