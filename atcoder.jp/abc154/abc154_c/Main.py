def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    beforeLen = len(num_list)

    num_list = set(num_list)

    afterLen = len(num_list)

    print('YES' if beforeLen == afterLen else 'NO')

if __name__ == '__main__':
    main()