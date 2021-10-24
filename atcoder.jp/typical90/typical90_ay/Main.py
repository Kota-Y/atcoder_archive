from itertools import product
from bisect import bisect_right
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def bit_search(A: list, l: int):
    num_list = [[] for _ in range(l + 1)]
    for i in product([0, 1], repeat = l):
        num = 0
        for j in range(l):
            if i[j] == 1:
                num += A[j]
        num_list[i.count(1)].append(num)
    
    for i in range(len(num_list)):
        num_list[i].sort()
    
    return num_list

def main():
    n, k, p = i_map()
    num_list = i_list()
    
    left = num_list[:n//2]
    right = num_list[n//2:]

    ans1_l = bit_search(left, len(left))
    ans2_l = bit_search(right, len(right))

    ans = 0
    for i in range(len(ans1_l)):
        num = k - i
        for j in range(len(ans1_l[i])):
            value = p - ans1_l[i][j]
            if num < 0 or value < 0: continue
            if not (0 <= num <= len(ans2_l) - 1): continue
            x = bisect_right(ans2_l[num], value)
            ans += x
    print(ans)

if __name__ == '__main__':
    main()
