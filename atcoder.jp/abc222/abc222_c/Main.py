import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import ceil, floor, sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def main():
    n, m = i_map()
    num_list = s_row_list(2*n)

    round_list = [0] * (2*n)

    q = deque()
    for i in range(n*2):
        q.append(i)

    for i in range(m):
        while len(q) != 0:
            a = q.popleft()
            b = q.popleft()
            if num_list[a][i] == 'G':
                if num_list[b][i] == 'P':
                    round_list[b] += 1     
                elif num_list[b][i] == 'C':
                    round_list[a] += 1                
            if num_list[a][i] == 'C':
                if num_list[b][i] == 'G':
                    round_list[b] += 1     
                elif num_list[b][i] == 'P':
                    round_list[a] += 1
            if num_list[a][i] == 'P':
                if num_list[b][i] == 'C':
                    round_list[b] += 1     
                elif num_list[b][i] == 'G':
                    round_list[a] += 1
        tmp_list = []
        for j in range(len(round_list)):
            tmp_list.append([round_list[j], j])
        tmp_list = sorted(tmp_list, key=lambda x: x[1])
        tmp_list = sorted(tmp_list, key=lambda x: -x[0])

        q = deque()
        for _, index in tmp_list:
            q.append(index)

    ans_list = []
    for j in range(len(round_list)):
        ans_list.append([round_list[j], j])
    ans_list = sorted(ans_list, key=lambda x: x[1])
    ans_list = sorted(ans_list, key=lambda x: -x[0])
    
    for _, ans in ans_list:
        print(ans+1)

if __name__ == '__main__':
    main()
