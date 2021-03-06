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
    n, m = i_map()
    num_list = i_list()
    
    tmp_list = set(num_list[:m])
    ans_min = INF

    tmp_co = Counter(num_list[:m])

    for i in range(max(num_list)+2):
        if i not in tmp_list:
            ans_min = i
            break


    for i in range(m, n):
        pop_num = num_list[i-m]
        insert_num = num_list[i]
        if pop_num == insert_num:
            continue
        if ans_min <= pop_num:
            tmp_co[pop_num] -= 1
            tmp_co[insert_num] += 1
            continue
        if tmp_co[pop_num] == 1:
            ans_min = pop_num
        tmp_co[pop_num] -= 1
        tmp_co[insert_num] += 1

    print(ans_min)

if __name__ == '__main__':
    main()
