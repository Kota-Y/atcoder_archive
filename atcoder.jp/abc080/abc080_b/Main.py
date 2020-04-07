def main():
    n = int(input())

    str_n = str(n)

    n_sum = 0

    for i in range(len(str_n)):
        n_sum += int(str_n[i])

    print('Yes' if n % n_sum == 0 else 'No')

if __name__ == '__main__':
    main()