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
def s_row_list(N): return [s_list() for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n = i_input()
    num_list = i_list()

    count = 0
    num_list.sort()
    max_num = num_list[n-1]
    ans_list = [0] * (max_num + 1)

    num_list_counter = Counter(num_list)

    for k, v in num_list_counter.items():
        if v == 1:
            continue
        ans_list[k] = 1

    for num in num_list:
        if ans_list[num] == 0:
            count += 1
        for i in range(num, max_num+1, num):
            ans_list[i] = 1

    print(count)
 
if __name__ == '__main__':
    main()
