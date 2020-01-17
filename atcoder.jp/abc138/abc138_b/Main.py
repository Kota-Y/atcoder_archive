def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    sum = 0
    tmp = 0

    for i in range(n):
        tmp += 1 / num_list[i]

    
    result = 1 / tmp

    print(result)

if __name__ == '__main__':
    main()