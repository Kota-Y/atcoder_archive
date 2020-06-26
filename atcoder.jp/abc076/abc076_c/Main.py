import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
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
    s = s_input()
    t = s_input()

    len_s = len(s)
    len_t = len(t)

    if len_s < len_t:
        print('UNRESTORABLE')
        exit()

    ans_list = []

    flag = False
    for i in range(len_s-len_t+1):
        tmp_s = s[i:i+len_t]
        for j in range(len_t):
            if tmp_s[j] != t[j] and tmp_s[j] != '?':
                break
        else:
            flag = True
            ans_s = s[0:i] + t + s[i+len_t:len_s]
            ans_list.append(ans_s.replace('?', 'a'))

    if not flag:
        print('UNRESTORABLE')
        exit()

    ans_list.sort()

    print(ans_list[0])
 
if __name__ == '__main__':
    main()
