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
    w, h, n = i_map()

    ans_list = [[1] * w for i in range(h)]

    for _ in range(n):
        x, y , a = i_map()

        if a == 1:
            for i in range(h):
                for j in range(x):
                    ans_list[i][j] = 0
        elif a == 2:
            for i in range(h):
                for j in range(x, w):
                    ans_list[i][j] = 0
        elif a == 3:
            for i in range(y):
                for j in range(w):
                    ans_list[i][j] = 0
        elif a == 4:
            for i in range(y, h):
                for j in range(w):
                    ans_list[i][j] = 0

    count = 0
    for i in range(h):
        for j in range(w):
            if ans_list[i][j] == 1:
                count += 1

    print(count)

if __name__ == '__main__':
    main()
