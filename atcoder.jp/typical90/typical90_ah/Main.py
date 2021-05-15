import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
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
    n, k = i_map()
    num_list = i_list()

    cr = 0
    count = 0
    ans = 0
    d = defaultdict(int)

    for i in range(n):
        while cr < n:
            # print(num_list[cr], cr,ans,count)
            # print(d)
            if d[num_list[cr]] == 0 and count == k:
                break
            if d[num_list[cr]] == 0:
                count += 1
            d[num_list[cr]] += 1
            cr += 1
        ans = max(ans, cr - i)
        if d[num_list[i]] == 1:
            count -= 1
        d[num_list[i]] -= 1
    
    print(ans)

if __name__ == '__main__':
    main()
