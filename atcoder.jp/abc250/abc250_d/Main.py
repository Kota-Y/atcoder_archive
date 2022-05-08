import sys, re
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import add, sub, mul, mod, xor
from math import sqrt, pi, factorial, gcd, sin, cos, atan2,degrees, radians, floor, ceil
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
# def ceil(a, b): return (a + b - 1) // b
# def floor(a, b): return a // b
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def create_prime_list(n: int) -> list:
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, n + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0

    prime_list = []
    for i, p in enumerate(primes):
        if p == 1:
            prime_list.append(i)
    
    return prime_list

def is_ok(arg, q3):
    return n >= arg * q3

def meguru_bisect(ng, ok, q):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, q3):
            ok = mid
        else:
            ng = mid
    return ok

n = i_input()

ans = 0

prime = create_prime_list(ceil(pow(n,1/3)+10))

for q in prime:
    q3 = pow(q, 3)
    if q3 > n:
        break

    res = meguru_bisect(q, 0, q3)
    co = bisect_right(prime, res)

    ans += co

print(ans)