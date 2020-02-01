def main():
    h, w = map(int, input().split())

    for _ in range(h):
        str_list = list(input().split())
        print(*str_list)
        print(*str_list)

if __name__ == '__main__':
    main()