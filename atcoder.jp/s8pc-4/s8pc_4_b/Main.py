from itertools import product

inf = 10 ** 19

def main():
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))

    ans = inf

    for bit in list(product([0, 1], repeat = n)):
        count = bit.count(1)
        if count < k:
            continue
        tmp = 0
        max_hight = 0
        for i in range(n):
            if bit[i] != 1:
                max_hight = max(max_hight, num_list[i])
                continue
            if max_hight >= num_list[i]:
                tmp += max_hight - num_list[i] + 1
                max_hight += 1
            else:
                max_hight = num_list[i]
        ans = min(ans, tmp)
    
    print(ans)

if __name__ == '__main__':
    main()