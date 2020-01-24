def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()

    for i in range(n-1):
        num_list[i+1] = (num_list[i]+num_list[i+1]) / 2

    print(num_list[n-1])

if __name__ == '__main__':
    main()