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
    num_list = i_row_list(m)
    k = i_input()
    k_list = i_row_list(k)

    ans = 0
    
    for bit in product([0,1], repeat=k):
        sara = [0] * n
        for i in range(k):
            if bit[i] == 0:
                sara[k_list[i][0]-1] += 1
            else:
                sara[k_list[i][1]-1] += 1
        tmp_count = 0
        for i in range(m):
            a, b = num_list[i][0], num_list[i][1]
            if sara[a-1] > 0 and sara[b-1] > 0:
                tmp_count += 1
        ans = max(ans, tmp_count)

    print(ans)

if __name__ == '__main__':
    main()
