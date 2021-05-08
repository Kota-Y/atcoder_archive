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
    n = i_input()
    num_list = i_row_list(n)
    
    h = 1001
    w = 1001

    list2 = [[0] * w for i in range(h)]
    ans_list = [[0] * w for i in range(h)]

    for i in range(n):
        lx, ly = num_list[i][0], num_list[i][1]
        rx, ry = num_list[i][2], num_list[i][3]
        list2[lx][ly] += 1
        list2[rx][ry] += 1
        list2[lx][ry] -= 1
        list2[rx][ly] -= 1

    for i in range(h):
        for j in range(1, w):
            list2[i][j] += list2[i][j-1]

    for i in range(w):
        for j in range(1, h):
            list2[j][i] += list2[j-1][i]
            
    ans_dict = defaultdict(int)

    for i in range(h):
        for j in range(w):
            if list2[i][j] == 0:
                continue
            ans_dict[list2[i][j]] += 1

    for check_num in range(1,n+1):
        print(ans_dict[check_num])

if __name__ == '__main__':
    main()
