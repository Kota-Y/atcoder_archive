def main():
    n = int(input())
    str_list = list(input().split())

    print('Four' if 'Y' in str_list else 'Three')


if __name__ == '__main__':
    main()