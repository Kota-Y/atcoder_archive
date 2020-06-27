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
    n, m, k = i_map()
    a_list = i_list()
    b_list = i_list()

    a_ruisekiwa = list(accumulate(a_list))
    b_ruisekiwa = list(accumulate(b_list))

    # print(a_ruisekiwa)
    # print(b_ruisekiwa)

    max_count = 0

    for i in range(n):
        if k < a_ruisekiwa[i]:
            break
        insert_num = k - a_ruisekiwa[i]
        insert_index = bisect_right(b_ruisekiwa, insert_num)
        max_count = max(max_count, i + insert_index +1)

    for i in range(m):
        if k < b_ruisekiwa[i]:
            break
        insert_num = k - b_ruisekiwa[i]
        insert_index = bisect_right(a_ruisekiwa, insert_num)
        max_count = max(max_count, i + insert_index +1)

    print(max_count)
 
if __name__ == '__main__':
    main()
