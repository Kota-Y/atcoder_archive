def main():
    n, k = map(int, input().split())

    ans = 0

    for i in range(1,n+1):
        count = 0
        while i < k:
            i *= 2
            count += 1
        ans += 1 / n * 0.5 ** count
        
    print(ans)

if __name__ == '__main__':
    main()