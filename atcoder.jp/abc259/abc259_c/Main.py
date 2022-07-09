import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians
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
def floor(a, b): return a // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    s = s_input()
    t = s_input()
    
    if s == t:
        print('Yes')
        exit()

    s_d = deque()
    s_d.append(s[0])
    co = 0
    for i in range(1, len(s)):
        before = s_d.pop()
        before_tmp = deepcopy(before)
        s_lower = before.lower()
        if s_lower != s[i]:
            s_d.append(before_tmp)
            s_d.append(str(co))
            s_d.append(s[i])
            co = 0
        else:
            co += 1
            s_upper = before.upper()
            s_d.append(s_upper)
    s_d.append(str(co))

    s_l = []
    while len(s_d) != 0:
        s_l.append(s_d.popleft())

    t_d = deque()
    t_d.append(t[0])
    co = 0
    for i in range(1, len(t)):
        before = t_d.pop()
        before_tmp = deepcopy(before)
        t_lower = before.lower()
        if t_lower != t[i]:
            t_d.append(before_tmp)
            t_d.append(str(co))
            t_d.append(t[i])
            co = 0
        else:
            co += 1
            t_upper = before.upper()
            t_d.append(t_upper)
    t_d.append(str(co)) 

    t_l = []
    while len(t_d) != 0:
        t_l.append(t_d.popleft())

    # print(s_l)
    # print(t_l)

    if len(s_l) != len(t_l):
        print('No')
        exit()
 
    al_l = ascii_lowercase
    al_u = ascii_uppercase

    for i in range(len(s_l)):
        if s_l[i] == t_l[i]:
            continue
        if s_l[i] in al_l or s_l[i] in al_u or t_l[i] in al_l or t_l[i] in al_u:
            print('No')
            exit()
        if int(s_l[i]) > int(t_l[i]):
            print('No')
            exit()

    print('Yes')

if __name__ == '__main__':
    main()
