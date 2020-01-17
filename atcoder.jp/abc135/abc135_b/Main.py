def main():
    n = int(input())
    num_list = list(map(int,input().split()))

    count = 0

    for i in range(0,n):
        if num_list[i] != i + 1:
            count += 1

    if count == 2 or count == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()