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
    a, b = i_map()

    a = str(a)
    b = str(b)
    
    max_ans = -INF
    for i in range(6):
        for j in range(10):
            if i == 0:
                if j == 0:
                    continue
                tmp_a = str(j) + a[1:]
                max_ans = max(max_ans, int(tmp_a)-int(b))
            elif i == 1:
                tmp_a = a[0] + str(j) + a[2]
                max_ans = max(max_ans, int(tmp_a)-int(b))
            elif i == 2:
                tmp_a = a[:2] + str(j)
                max_ans = max(max_ans, int(tmp_a)-int(b))
            if i == 3:
                if j == 0:
                    continue
                tmp_b = str(j) + b[1:]
                max_ans = max(max_ans, int(a)-int(tmp_b))
            elif i == 4:
                tmp_b = b[0] + str(j) + b[2]
                max_ans = max(max_ans, int(a)-int(tmp_b))
            elif i == 5:
                tmp_b = b[:2] + str(j)
                max_ans = max(max_ans, int(a)-int(tmp_b))
    print(max_ans)

if __name__ == '__main__':
    main()
