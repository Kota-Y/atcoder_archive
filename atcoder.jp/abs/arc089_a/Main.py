def main():
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        t = num_list[i][0]
        xy = num_list[i][1] + num_list[i][2]
        if t < num_list[i][1] or t < num_list[i][2]:
            print('No')
            exit()
        if t < xy:
            print('No')
            exit()
        if t % 2 == 0 and xy % 2 != 0:
            print('No')
            exit()
        if t % 2 != 0 and xy % 2 == 0:
            print('No')
            exit()


    print('Yes')

if __name__ == '__main__':
    main()