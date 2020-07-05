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
def s_row_list(N): return [s_list() for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    h, w, K = i_map()
    str_list = s_row_list(h)

    count = 0

    for h_bit in list(product([0,1], repeat=h)):
        for w_bit in list(product([0,1], repeat=w)):
            copy_list = deepcopy(str_list)

            for i in range(h):
                if h_bit[i] == 0:
                    continue
                copy_list[i][0] = '.' * w

            for i in range(w):
                if w_bit[i] == 0:
                    continue
                for k in range(h):
                    tmp = ''
                    for l in range(w):
                        if l == i:
                            tmp += '.'
                        else:
                            tmp += copy_list[k][0][l]
                    copy_list[k][0] = tmp
            tmp_count = 0
            for aaa in range(h):
                for bbb in range(w):
                    if copy_list[aaa][0][bbb] == '.':
                        continue
                    tmp_count += 1
            if tmp_count == K:
                count += 1

    print(count)
 
if __name__ == '__main__':
    main()
