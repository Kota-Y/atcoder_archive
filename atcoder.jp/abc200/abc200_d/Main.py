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
    num_list = i_list()

    ans_list = [[] for i in range(200)]

    n = min(n, 8)

    for bit in product([0,1], repeat=n):
        tmp_count = 0
        tmp_list = []

        for i in range(n):
            if bit[i] == 0:
                continue
            tmp_count += num_list[i]
            tmp_list.append(i+1)
        tmp_count %= 200
        if len(ans_list[tmp_count]) != 0:
            print('Yes')
            print(len(ans_list[tmp_count]), *ans_list[tmp_count])
            print(len(tmp_list), *tmp_list)
            exit()
        else:
            ans_list[tmp_count] = tmp_list
    
    print('No')

if __name__ == '__main__':
    main()
