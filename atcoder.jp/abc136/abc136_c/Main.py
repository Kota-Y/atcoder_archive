def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    flag = True

    for i in range(n-1):
        if num_list[i] != 1 and num_list[i-1] < num_list[i]:
            num_list[i] -= 1
        if num_list[i]  > num_list[i+1]:
            flag = False
            break
            
    print('Yes' if flag else 'No')

if __name__ == '__main__':
    main()