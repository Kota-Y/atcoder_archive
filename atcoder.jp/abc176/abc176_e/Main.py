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
    h, w, m = i_map()
    num_list = i_row_list(m)

    if h == 1 or w == 1:
        print(m)
        exit()

    h_list = []
    w_list = []

    count = 0

    for num in num_list:
        h_list.append(num[0])
        w_list.append(num[1])

    co_h_list = Counter(h_list)
    co_w_list = Counter(w_list)

    # print(num_list)
    # print(co_h_list.most_common())
    # print(co_w_list.most_common())

    h_max_key = co_h_list.most_common()[0][0]
    h_max_value = co_h_list.most_common()[0][1]

    w_max_key = co_w_list.most_common()[0][0]
    w_max_value = co_w_list.most_common()[0][1]

    if h_max_value > w_max_value:
        max_index = h_max_key
        count = h_max_value

        tmp_list = []
        for num in num_list:
            if num[0] == max_index:
                continue
            tmp_list.append(num[1])

        if len(tmp_list) != 0:
            count += Counter(tmp_list).most_common()[0][1]
    elif h_max_value == w_max_value:
        max_index = h_max_key
        h_count = h_max_value

        tmp_list = []
        for num in num_list:
            if num[0] == max_index:
                continue
            tmp_list.append(num[1])

        if len(tmp_list) != 0:
            h_count += Counter(tmp_list).most_common()[0][1]     


        max_index = w_max_key
        w_count = w_max_value

        tmp_list = []
        for num in num_list:
            if num[1] == max_index:
                continue
            tmp_list.append(num[0])

        if len(tmp_list) != 0:  
            w_count += Counter(tmp_list).most_common()[0][1]

        count = max(h_count, w_count)
    else:
        max_index = w_max_key
        count = w_max_value

        tmp_list = []
        for num in num_list:
            if num[1] == max_index:
                continue
            tmp_list.append(num[0])

        if len(tmp_list) != 0:  
            count += Counter(tmp_list).most_common()[0][1]

    print(count)

if __name__ == '__main__':
    main()
