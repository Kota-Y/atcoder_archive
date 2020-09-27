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
    id, n, k = i_map()
    str_list = s_row_list(n)
    
    join_list = []
    for i in range(n):
        join_list += str_list[i]

    pick_color = Counter(join_list).most_common()[1][0]
    pick_num = Counter(join_list).most_common()[1][1]

    query_num = n * n - pick_num
    print(query_num)

    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if str_list[i-1][j-1] == pick_color:
                continue
            print(j, i, pick_color)

if __name__ == '__main__':
    main()
