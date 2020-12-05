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

def lcm_base(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)
def lcm_list(num_list: list):
    return reduce(lcm_base, num_list, 1)

def main():
    n = i_input()

    tmp_list = []

    for i in range(2, n+1):
        tmp_list.append(i)

    lcm_num = lcm_list(tmp_list)
    
    i = 1
    while True:
        tmp = lcm_num * i + 1
        for a in tmp_list:
            if tmp % a != 1:
                break
        else:
            print(tmp)
            exit()
        i += 1


if __name__ == '__main__':
    main()
