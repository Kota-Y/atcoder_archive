def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    sumLs = sum(num_list)

    minCount = 10**9

    left = 0
    right = 0

    for i in range(n):
        left += num_list[i]
        right = sumLs - left
        minCount = min(abs(left-right),minCount)

    print(minCount)

if __name__ == '__main__':
    main()