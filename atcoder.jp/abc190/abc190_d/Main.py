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

def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            # if i != n // i:
            #     return_list.append(n//i)

    return return_list

def main():
    n = i_input()
    
    ans = 0

    num_list = make_divisors(n*2)

    for num in num_list:
        if num == 1:
            ans += 1
            continue
        tmp = 2 * n // num
        left = 0
        right = tmp
        while left + 1< right:
            middle = (left+right) // 2
            b = middle + num - 1
            if middle + b == tmp:
                ans += 1
                break
            elif middle + b < tmp:
                left = middle
            elif middle + b > tmp:
                right = middle 

    print(ans*2)

if __name__ == '__main__':
    main()