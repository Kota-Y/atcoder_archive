def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    c_num_list = num_list[:]

    num_list.sort()

    for i in range(n):
        tmp = num_list[n//2]
        if c_num_list[i] >= tmp:
            print(num_list[n//2-1])
        else:
            print(num_list[n//2])
        

if __name__ == '__main__':
    main()