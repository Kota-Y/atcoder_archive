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

def f(x, y , z):
    return x * x + y * y + z * z + x * y + y * z + z * x

def main():
    n = i_input()

    ans_list = []
    max_num = ceil(sqrt(n))
    for x in range(1,max_num):
        for y in range(1, max_num):
            for z in range(1, max_num):
                ans_list.append([x, y, z])
    
    result_list = []
    for x, y ,z in ans_list:
        result_list.append(f(x, y, z))

    result_dict = Counter(result_list)

    for i in range(1, n+1):
        print(result_dict[i])

if __name__ == '__main__':
    main()
