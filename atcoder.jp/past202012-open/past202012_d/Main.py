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
    str_list = s_row(n)

    ans_list = []
    for i in range(n):
        ans_list.append([int(str_list[i]), i])            

    ans_list.sort()

    ans_sub = []
    for i in range(n):
        ans_sub.append(ans_list[i][0])
    ans_co = Counter(ans_sub)

    tmp = []

    i = 0
    while i < n:
        tmp_i = ans_list[i][0]
        for j in range(ans_co[tmp_i]):
            tmp.append(str_list[ans_list[i+j][1]])

        if tmp_i == 0:
            tmp.sort(reverse=True)
        else:
            tmp.sort()
        for s in tmp:
            print(s)
        tmp = []
        
        i += ans_co[tmp_i]

if __name__ == '__main__':
    main()
