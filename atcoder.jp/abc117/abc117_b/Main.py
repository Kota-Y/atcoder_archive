def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    max_num = max(num_list)

    num_list.remove(max_num)

    sum_list = sum(num_list)

    if sum_list > max_num:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()