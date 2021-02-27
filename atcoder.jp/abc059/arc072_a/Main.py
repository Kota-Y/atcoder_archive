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
    n = i_input()
    num_list = i_list()

    count_plus = 0
    curren_num = 0
    isPlus = True
    for i in range(n):
        curren_num += num_list[i]
        if isPlus:
            if curren_num >= 0:
                count_plus += curren_num + 1
                curren_num = -1
        else:
            if curren_num <= 0:
                count_plus += -1 * curren_num + 1
                curren_num = 1
        isPlus = not isPlus

    count_minus = 0
    curren_num = 0
    isPlus = False
    for i in range(n):
        curren_num += num_list[i]
        if isPlus:
            if curren_num >= 0:
                count_minus += curren_num + 1
                curren_num = -1
        else:
            if curren_num <= 0:
                count_minus += -1 * curren_num + 1
                curren_num = 1
        isPlus = not isPlus

    print(min(count_minus, count_plus))

if __name__ == '__main__':
    main()
