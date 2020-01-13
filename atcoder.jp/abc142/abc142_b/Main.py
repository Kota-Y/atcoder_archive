def main():
    n, k = map(int, input().split())
    num_list = list(map(int, input().split()))

    count = 0

    for i in range(n):
        if num_list[i] >= k:
            count +=1

    print(count)

if __name__ == '__main__':
    main()