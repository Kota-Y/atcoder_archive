def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    count = n

    min = num_list[0]

    for i in range(1,n):
        if num_list[i] > min:
            count -= 1
        if num_list[i] < min:
            min = num_list[i]

    print(count)

if __name__ == '__main__':
    main()