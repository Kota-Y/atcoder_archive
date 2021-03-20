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
    s_n = str(n)
    
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    ans = 0

    for v in product(l, repeat=1):
        if v[0] == '0':
            continue
        tmp = v[0]
        tmptmp = tmp + tmp
        if int(tmptmp) > n:
            print(ans)
            exit()
        ans += 1

    for v in product(l, repeat=2):
        if v[0] == '0':
            continue
        tmp = v[0] + v[1]
        tmptmp = tmp + tmp
        if int(tmptmp) > n:
            print(ans)
            exit()
        ans += 1

    for v in product(l, repeat=3):
        if v[0] == '0':
            continue
        tmp = v[0] + v[1] + v[2]
        tmptmp = tmp + tmp
        if int(tmptmp) > n:
            print(ans)
            exit()
        ans += 1

    for v in product(l, repeat=4):
        if v[0] == '0':
            continue
        tmp = v[0] + v[1] + v[2] + v[3]
        tmptmp = tmp + tmp
        if int(tmptmp) > n:
            print(ans)
            exit()
        ans += 1

    for v in product(l, repeat=5):
        if v[0] == '0':
            continue
        tmp = v[0] + v[1] + v[2] + v[3] + v[4]
        tmptmp = tmp + tmp
        if int(tmptmp) > n:
            print(ans)
            exit()
        ans += 1


    for v in product(l, repeat=6):
        if v[0] == '0':
            continue
        tmp = v[0] + v[1] + v[2] + v[3] + v[4] + v[5]
        tmptmp = tmp + tmp
        if int(tmptmp) > n:
            print(ans)
            exit()
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
