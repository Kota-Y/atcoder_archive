def main():
    n, m = map(int, input().split())
    num_list = []
    for _ in range(m):
        num_list.append(list(map(int,input().split())))

    for i in range(1000):
        if len(str(i)) != n:
            continue
        for j in range(m):
            tmp = int(str(i)[num_list[j][0]-1])
            if num_list[j][1] != tmp:
                break
        else:
            print(i)
            exit()

    print(-1)

if __name__ == '__main__':
    main()