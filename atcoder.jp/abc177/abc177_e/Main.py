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

def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)

def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n//i)

    return return_list[2:]

def main():
    n = i_input()
    num_list = i_list()

    num_list = list(set(num_list))

    if gcd_list(num_list) != 1:
        print('not coprime')
        exit()

    num_list.sort()

    tmp_list = [0] * (num_list[0-1] + 1)

    for num in num_list:
        if tmp_list[num] == 1:
            print('setwise coprime')
            exit()

        yakusu_list = make_divisors(num)
        yakusu_list.sort()

        for yakusu in yakusu_list:
            for i in range(yakusu, num_list[-1], yakusu):
                tmp_list[i] = 1

        for i in range(num, num_list[-1], num):
            tmp_list[i] = 1

    print('pairwise coprime')

if __name__ == '__main__':
    main()
