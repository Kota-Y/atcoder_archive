def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    
    count = 0

    max = 0

    num_list.reverse()

    for i in range(n-1):
        if num_list[i] <= num_list[i+1]:
            count += 1
        else:
            count = 0
        if max < count:
            max = count

    print(max)

if __name__ == '__main__':
    main()