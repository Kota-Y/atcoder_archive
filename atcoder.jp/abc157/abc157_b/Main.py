def main():
    num_list = []
    for _ in range(3):
        num_list.append(list(map(int,input().split())))
    n = int(input())
    b_list = [int(input()) for _ in range(n)]

    for i in range(3):
        for j in range(3):
            if num_list[i][j] in b_list:
                num_list[i][j] = '!'

    for i in range(3):
        count = 0
        for j in range(3):
            if num_list[i][j] == '!':
                count += 1
        if count == 3:
            print('Yes')
            exit()

    for i in range(3):
        count = 0
        for j in range(3):
            if num_list[j][i] == '!':
                count += 1
        if count == 3:
            print('Yes')
            exit()
    
    if num_list[0][0] == '!' and num_list[1][1] == '!' and num_list[2][2] == '!':
        print('Yes')
        exit()

    if num_list[0][2] == '!' and num_list[1][1] == '!' and num_list[2][0] == '!':
        print('Yes')
        exit()

    print('No')

if __name__ == '__main__':
    main()