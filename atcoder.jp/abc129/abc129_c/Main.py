def main():
    n, m = map(int, input().split())
    num_list = [int(input()) for _ in range(m)]

    dp = [0] * (n+1)
    dp[0] = 1
    
    for num in num_list:
        dp[num] = -1

    if dp[1] != -1:
        dp[1] = 1
    else:
        dp[1] = 0

    for i in range(2,n+1):
        if dp[i] == -1:
            dp[i] = 0
            continue
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n]%1000000007)

if __name__ == '__main__':
    main()