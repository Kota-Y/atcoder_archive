import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
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
    s1 = s_input()
    s2 = s_input()
    s3 = s_input()

    tmp_set = set()
    for i in s1:
        tmp_set.add(i)
    for i in s2:
        tmp_set.add(i)
    for i in s3:
        tmp_set.add(i)

    tmp_list = list(tmp_set)

    if len(tmp_set) > 10:
        print('UNSOLVABLE')
        exit()

    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for v in list(permutations(l, len(tmp_set))):
        tmp1 = ''
        skip_flag = False
        for i in range(len(s1)):
            tmp = v[tmp_list.index(s1[i])]
            if i == 0 and tmp == '0':
                skip_flag = True
                continue
            else:
                tmp1 += tmp
        if skip_flag:
            continue
        tmp2 = ''
        for i in range(len(s2)):
            tmp = v[tmp_list.index(s2[i])]
            if i == 0 and tmp == '0':
                skip_flag = True
                continue
            else:
                tmp2 += tmp
        if skip_flag:
            continue
        tmp3 = ''
        for i in range(len(s3)):
            tmp = v[tmp_list.index(s3[i])]
            if i == 0 and tmp == '0':
                skip_flag = True
                continue
            else:
                tmp3 += tmp
        if skip_flag:
            continue

        tmp1_i = int(tmp1)
        tmp2_i = int(tmp2)
        tmp3_i = int(tmp3)

        if tmp1_i + tmp2_i == tmp3_i:
            print(tmp1_i)
            print(tmp2_i)
            print(tmp3_i)
            exit()

    print('UNSOLVABLE')

if __name__ == '__main__':
    main()
