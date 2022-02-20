import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import floor, sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
from copy import deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from array import array
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
def ceil(a, b): return (a + b - 1) // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n, x = i_map()
    num_list = i_row_list(n)
    
    sum_set1 = set()
    sum_set1.add(num_list[0][0])
    sum_set1.add(num_list[0][1])

    for i in range(1,n):
        a, b = num_list[i][0], num_list[i][1]

        if i % 2 == 1:
            sum_set2 = set()
            for tmp in sum_set1:
                tmp_ans1 = tmp + a
                if tmp_ans1 + (n-i-1) <= x:
                    sum_set2.add(tmp_ans1)
                tmp_ans2 = tmp + b
                if tmp_ans2 + (n-i-1) <= x:
                    sum_set2.add(tmp_ans2)
        else:
            sum_set1 = set()
            for tmp in sum_set2:
                tmp_ans1 = tmp + a
                if tmp_ans1 + (n-i-1) <= x:
                    sum_set1.add(tmp_ans1)
                tmp_ans2 = tmp + b
                if tmp_ans2 + (n-i-1) <= x:
                    sum_set1.add(tmp_ans2)

    # print(sum_set1)
    # print(sum_set2)

    if n % 2 == 0:
        if x in sum_set2:
            print('Yes')
        else:
            print('No')
    else:
        if x in sum_set1:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
