def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    for i in range(n):
        if num_list[i] % 2 == 0:
            if num_list[i] % 3 == 0 or num_list[i] % 5 == 0:
                continue
            else:
                print('DENIED')
                exit()

    print('APPROVED')

if __name__ == '__main__':
    main()