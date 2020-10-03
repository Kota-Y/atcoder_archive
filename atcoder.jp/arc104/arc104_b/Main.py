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
    n, s = s_map()

    n = int(n)

    a_list = [0] * (n+1)
    t_list = [0] * (n+1)
    g_list = [0] * (n+1)
    c_list = [0] * (n+1)

    for i in range(n):
        a_list[i+1] = a_list[i]
        t_list[i+1] = t_list[i]
        g_list[i+1] = g_list[i]
        c_list[i+1] = c_list[i]

        if s[i] == 'A':
            a_list[i+1] += 1
        elif s[i] == 'T':
            t_list[i+1] += 1
        elif s[i] == 'G':
            g_list[i+1] += 1
        elif s[i] == 'C':
            c_list[i+1] += 1

    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a_list[j+1] - a_list[i] == t_list[j+1] - t_list[i] and g_list[j+1] - g_list[i] == c_list[j+1] - c_list[i]:
                count += 1
            
    print(count)

if __name__ == '__main__':
    main()
