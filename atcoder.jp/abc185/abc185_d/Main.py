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
    num_list = i_list()

    if m == 0:
        print(1)
        exit()

    if n == m:
        print(0)
        exit()

    num_list.sort()

    kukan_list = []
    start = 1
    for num in num_list:
        tmp = num - start
        if tmp != 0:
            kukan_list.append(tmp)
        start = num + 1


    tmp = n-start+1
    if tmp != 0:
        kukan_list.append(tmp)

    kukan_list.sort()

    min_kukan = kukan_list[0]

    count = 0
    for kukan in kukan_list:
        tmp = ceil(kukan / min_kukan)
        count += tmp

    print(count)

if __name__ == '__main__':
    main()
