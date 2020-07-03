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
    n, m = i_map()
    a_list = i_list()
    num_list = i_row_list(m)

    a_list.sort(reverse=True)
    num_list = sorted(num_list, key=lambda x: -x[1])

    ans = 0
    a_count = 0
    num_count = 0
    for _ in range(n):
        if num_count == m or a_list[a_count] > num_list[num_count][1]:
            ans += a_list[a_count]
            a_count += 1
        else:
            ans += num_list[num_count][1]
            num_list[num_count][0] -= 1
            if num_list[num_count][0] == 0:
                num_count += 1
    print(ans)

if __name__ == '__main__':
    main()
