def main():
    n, m = map(int, input().split())

    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    ans = 0
    for i in range(m):
        for j in range(i+1,m):
            tmp = 0
            for k in range(n):
                tmp += max(num_list[k][i], num_list[k][j])
            ans = max(ans, tmp)
        
    print(ans)

if __name__ == '__main__':
    main()