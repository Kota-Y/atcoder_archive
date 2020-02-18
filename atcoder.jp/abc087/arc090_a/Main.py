def main():
    n = int(input())
    num_list = []
    for _ in range(2):
        num_list.append(list(map(int,input().split())))

    ans = 0

    for i in range(n):
        point = 0
        tmp = num_list[0][0]
        for j in range(n):
            if i == j:
                point = 1
                tmp += num_list[point][j]
            else:
                tmp += num_list[point][j+1-point]
        ans = max(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()