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
    n, t = i_map()
    num_list = i_list()

    a_list = num_list[:n//2]
    b_list = num_list[n//2:]

    a_sum_list = []
    for bit in product([0,1], repeat=len(a_list)):
        tmp_sum = 0
        for i in range(len(a_list)):
            if bit[i] == 0:
                continue
            tmp_sum += a_list[i]
        a_sum_list.append(tmp_sum)
            
    b_sum_list = []
    for bit in product([0,1], repeat=len(b_list)):
        tmp_sum = 0
        for i in range(len(b_list)):
            if bit[i] == 0:
                continue
            tmp_sum += b_list[i]
        b_sum_list.append(tmp_sum)

    a_sum_list = list(set(a_sum_list))
    b_sum_list = list(set(b_sum_list))

    a_sum_list.sort()
    b_sum_list.sort()

    ans = 0
    for num in a_sum_list:
        insert_index = bisect_right(b_sum_list, t-num)
        if num+b_sum_list[insert_index-1] <= t:
            ans = max(ans, num+b_sum_list[insert_index-1])

    print(ans)

if __name__ == '__main__':
    main()
