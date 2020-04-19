def main():
    n = int(input())
    str_list = [input() for _ in range(n)]

    if len(str_list) != len(set(str_list)):
        print('No')
        exit()

    for i in range(1,n):
        if str_list[i-1][-1] != str_list[i][0]:
            print('No')
            exit()

    print('Yes')

if __name__ == '__main__':
    main()