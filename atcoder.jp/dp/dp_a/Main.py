def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(num_list[1]-num_list[0])
    
    for i in range(2,n):
        dp[i] = min(abs(num_list[i-1]-num_list[i])+dp[i-1], abs(num_list[i-2]-num_list[i])+dp[i-2])
    
    print(dp[n-1])

if __name__ == '__main__':
    main()