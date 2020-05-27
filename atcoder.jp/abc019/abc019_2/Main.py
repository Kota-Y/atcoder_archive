import sys, re
from math import ceil, floor, sqrt, pi, factorial#, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
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
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    s = s_input()

    ans_list = []

    tmp_s = s[0]
    tmp_c = 1
    for i in range(1,len(s)):
        if tmp_s == s[i]:
            tmp_c += 1
        else:
            ans_list.append(tmp_s)
            ans_list.append(tmp_c)
            tmp_s = s[i]
            tmp_c = 1

    ans_list.append(tmp_s)
    ans_list.append(tmp_c)

    ans_str = ''
    for i in range(len(ans_list)):
        if i % 2 == 0:
            ans_str += ans_list[i]
        else:
            ans_str += str(ans_list[i])
        
    print(ans_str)
            
if __name__ == '__main__':
    main()
