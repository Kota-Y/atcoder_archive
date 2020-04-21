def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    count = 0
    search_num = 1

    for num in num_list:
        if search_num == num:
            search_num += 1
            continue
        count += 1
        
    print(count if search_num != 1 else -1)

if __name__ == '__main__':
    main()