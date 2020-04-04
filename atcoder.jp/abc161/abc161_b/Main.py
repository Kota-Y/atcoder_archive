def main():
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    vote_num = sum(num_list)

    count = 0

    for i in range(n):
        if vote_num * 1/(4*m) <= num_list[i]:
            count += 1

    print('Yes' if count >= m else 'No')

if __name__ == '__main__':
    main()