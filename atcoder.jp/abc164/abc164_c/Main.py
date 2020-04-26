def main():
    n = int(input())
    str_list = [input() for _ in range(n)]



    print(len(set(str_list)))

if __name__ == '__main__':
    main()