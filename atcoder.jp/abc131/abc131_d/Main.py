def main():
    n = int(input())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    num_list = sorted(num_list, key=lambda x: x[1])
        
    time = 0
    for i in range(n):
        time += num_list[i][0]
        if time > num_list[i][1]:
            print('No')
            exit()

    print('Yes')

if __name__ == '__main__':
    main()