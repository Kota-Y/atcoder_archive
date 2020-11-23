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
    r1, c1 = i_map()
    r2, c2 = i_map()

    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1-r2) + abs(c1-c2) <= 3:
        print(1)
        exit()

    if (r1+r2+c1+c2) % 2 == 0:
        print(2)
        exit()

    if abs(r1-r2) + abs(c1-c2) <= 6:
        print(2)
        exit()

    if abs(r1-r2+c1-c2) <= 3 or abs(r1-r2-c1+c2) <= 3: 
        print(2)
        exit()

    print(3)

if __name__ == '__main__':
    main()
