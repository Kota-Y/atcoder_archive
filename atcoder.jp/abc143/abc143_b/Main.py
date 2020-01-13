def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    result = 0

    for i in range(n):
        for j in range(n):
            if i == j or i > j:
                continue
            result += num_list[i] * num_list[j]

    print(result)

if __name__ == '__main__':
    main()