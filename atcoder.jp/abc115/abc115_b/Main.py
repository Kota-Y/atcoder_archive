def main():
    n = int(input())
    num_list = [int(input()) for _ in range(n)]

    num_list.sort(reverse=True)

    count = 0

    for i in range(n):
        if i == 0:
            count += num_list[i] // 2
        else:
            count += num_list[i]

    print(count)

if __name__ == '__main__':
    main()