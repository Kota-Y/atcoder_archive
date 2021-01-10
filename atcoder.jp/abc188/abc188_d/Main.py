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
    n, C = i_map()
    num_list = i_row_list(n)

    ans_list = []

    for i in range(n):
        a, b, c = num_list[i][0], num_list[i][1], num_list[i][2]
        ans_list.append([a,c])
        ans_list.append([b+1,-c])
    
    ans_list.sort()


    tmp_list = []
    for i in range(2*n):
        current = ans_list[i][0]
        if i == 2*n-1:
            tmp_list.append(ans_list[i])
        else:
            next = ans_list[i+1][0]
            if current != next:
                tmp_list.append(ans_list[i])
            else:
                ans_list[i+1][1] += ans_list[i][1]
            
    ans = 0
    plus = 0
    for i in range(len(tmp_list)-1):
        plus += tmp_list[i][1]
        current = tmp_list[i][0]
        next = tmp_list[i+1][0]
        add = plus * (next-current)
        if plus <= C:
            ans += add
        else:
            ans += C * (next-current)

    print(ans)

if __name__ == '__main__':
    main()
