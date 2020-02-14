def main():
    n, m, c = map(int, input().split())

    b_list = list(map(int, input().split()))

    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    count = 0

    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += num_list[i][j] * b_list[j]
        if tmp + c > 0:
            count += 1

    print(count)

if __name__ == '__main__':
    main()