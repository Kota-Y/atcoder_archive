def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    count = 0

    for i in range(1,n-1):
        if max(num_list[i-1],num_list[i],num_list[i+1]) != num_list[i]:
            if min(num_list[i-1],num_list[i],num_list[i+1]) != num_list[i]:
                count += 1

    print(count)

 
if __name__ == '__main__':
    main()