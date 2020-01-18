def main():
    num_list = list(map(int,input().split()))

    good_list = [1,4,7,9]

    num_list.sort()

    if num_list == good_list:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
