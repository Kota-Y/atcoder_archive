def main():
    num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

    result = 0

    for i in range(len(num_list)):
        result += num_list[i]


    if result >= 22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()