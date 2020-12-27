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

def sieve_eratosthenes(n):
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


def isPrime(n, prime_list):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
  
    m = floor(sqrt(n))
    for p in prime_list:
        if n % p == 0:
            return False
        if p > m:
            # 素数がnの平方根を超えたら終了
            break
    return True

def main():
    q = i_input()

    tmp_list = [0]
    prime_list = sieve_eratosthenes(10**5+1)

    for i in range(1, 10**5+1):
        if i % 2 == 0:
            tmp_list.append(0)
            continue
        if isPrime(i, prime_list) and isPrime((i+1)//2, prime_list):
            tmp_list.append(1)
        else:
            tmp_list.append(0)

    ruisekiwa = list(accumulate(tmp_list))

    for _ in range(q):
        l, r = i_map()
        print(ruisekiwa[r]-ruisekiwa[l-1])

if __name__ == '__main__':
    main()
