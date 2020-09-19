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
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n, x, m = i_map()

    if x == 0:
        print(0)
        exit()

    ans = x
    tmp = x

    tmp_list = [x]

    has_find = False

    for i in range(n-1):
        if tmp*tmp%m in tmp_list:
            before_index = tmp_list.index(tmp*tmp%m)
            loop_list = []
            for l in range(before_index, i+1):
                loop_list.append(tmp_list[l])
            has_find = True
            break
        tmp_list.append(tmp*tmp%m)
        tmp = tmp*tmp%m
        ans += tmp

    if not has_find:
        print(ans)
        exit()

    # print(i,before_index)
    # print(loop_list)

    if before_index == 0:
        ans = 0
    else:
        ans = x
    tmp = x
    for _ in range(before_index-1):
        tmp = tmp*tmp%m
        ans += tmp

    n -= before_index

    loop_sum = sum(loop_list)

    loop_num = n // len(loop_list)
    mod_num = n % len(loop_list)

    ans += loop_sum * loop_num

    for i in range(mod_num):
        ans += loop_list[i]

    print(ans)

if __name__ == '__main__':
    main()
