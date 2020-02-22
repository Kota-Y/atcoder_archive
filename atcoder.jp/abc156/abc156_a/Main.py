def main():
    n, k = map(int, input().split())

    ans = 0

    if n >= 10:
        ans = k
    else:
        ans = k + 100 * (10-n)
    
    print(ans)

if __name__ == '__main__':
    main()