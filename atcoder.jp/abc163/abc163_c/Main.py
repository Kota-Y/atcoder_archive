def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    result_list = [0]*n

    for i in range(n-1):
        result_list[num_list[i]-1] += 1

    for i in range(n):
        print(result_list[i])

if __name__ == '__main__':
    main()
