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
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

class SegmentTree(object):
	def __init__(self, N):
		self.N = N
		self.N0 = 2 ** (N - 1).bit_length()
		self.initVal = 0
		self.data = [self.initVal] * (2 * self.N0)
 
	# 区間クエリの種類
	def calc(self, a, b):
		return max(a, b)
 
	#k番目の値をxに更新
	def update(self, k, x):
		k += self.N0 - 1
		self.data[k] = x
		while k > 0:
			k = (k - 1) // 2
			self.data[k] = self.calc(self.data[2 * k + 1], self.data[2 * k + 2])
 
	#区間[l, r]の演算値
	def query(self, l, r):
		L = l + self.N0; R = r + self.N0 + 1
		m = self.initVal
		while L < R:
			if R & 1:
				R -= 1
				m = self.calc(m, self.data[R - 1])
			if L & 1:
				m = self.calc(m, self.data[L - 1])
				L += 1
			L >>= 1; R >>= 1
 
		return m

def main():
    n, k = i_map()
    size = 300000 + 2
    seg = SegmentTree(size)
    for _ in range(n):
        a = i_input()
        l = max(0, a -k)
        r = min(size - 1, a + k)
        res = seg.query(l, r)
        seg.update(a, res + 1)
 
    ans = seg.query(0, size - 1)
    print(ans)

if __name__ == '__main__':
    main()
