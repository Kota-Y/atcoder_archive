from itertools import accumulate    # 累積和: list(accumulate(num_list))

def main():
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))

    compute_list = []

    for num in num_list:
        compute_list.append((1+num)/2)

    sum_list = list(accumulate(compute_list))

    if k == n:
        print(sum_list[k-1])
        exit()

    ans = 0

    for i in range(n-k):
        ans = max(ans, sum_list[i+k] - sum_list[i])

    print(ans)

if __name__ == '__main__':
    main()