def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    for i in range(n):
        num_list[i] -= 1

    count = 0
    for i in range(n-1):
        if num_list[i] == i:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            count += 1

    if num_list[n-1] == n-1:
        num_list[i], num_list[i-1] = num_list[i-1], num_list[i]
        count += 1

    print(count)

if __name__ == '__main__':
    main()