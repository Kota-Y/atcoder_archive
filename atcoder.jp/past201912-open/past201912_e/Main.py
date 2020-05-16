import sys, re
from math import ceil, floor, sqrt, pi, factorial#, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left
from functools import reduce
input = sys.stdin.readline 
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
    n, q = i_map()
    num_list = i_row_list(q)

    list2 = [['N'] * n for i in range(n)]

    for i in range(q):
        case_num = num_list[i][0]
        if case_num == 1:
            list2[num_list[i][1]-1][num_list[i][2]-1] = 'Y'
        elif case_num == 2:
            for j in range(n):
                if list2[j][num_list[i][1]-1] == 'Y':
                    list2[num_list[i][1]-1][j] = 'Y'
        elif case_num == 3:
            follow_list = []
            for j in range(n):
                if list2[num_list[i][1]-1][j] == 'Y':
                    follow_list.append(j)
            for follow in follow_list:
                for j in range(n):
                    if num_list[i][1] == j + 1:
                        continue
                    if list2[follow][j] == 'Y':
                        list2[num_list[i][1]-1][j] = 'Y'

    for ll in list2:
        for l in ll:
            print(l, end='')
        print()
        
if __name__ == '__main__':
    main()
