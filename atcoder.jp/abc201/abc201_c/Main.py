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
    s = s_input()

    ok_list = []
    dame_list = []

    for i, tmp_s in enumerate(s):
        if tmp_s in'o':
            ok_list.append(str(i))
        if tmp_s in'x':
            dame_list.append(str(i))

    l = digits
    ans = 0
    for bit in product(l, repeat=4):
        for i in range(4):
            if bit[i] in dame_list:
                break
        else:
            ok_num = 0
            for i in range(len(ok_list)):
                check_num = ok_list[i]
                flag = False
                for j in range(4):
                    if check_num == bit[j]:
                        flag = True
                        break
                if flag:
                    ok_num += 1
            if ok_num == len(ok_list):
                ans += 1

    print(ans)
    
if __name__ == '__main__':
    main()
