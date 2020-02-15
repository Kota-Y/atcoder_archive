def main():
    n, m = map(int, input().split())
    num_list = []
    for _ in range(n):
        num_list.append(list(map(int,input().split())))

    ans = 0

    num_list = sorted(num_list, key=lambda x: x[0])

    for i in range(n):
        if m <= 0:
            break
        if m >= num_list[i][1]:
            ans += num_list[i][0] * num_list[i][1]
            m -= num_list[i][1]
        else:
            ans += num_list[i][0] * m
            break

    print(ans)

if __name__ == '__main__':
    main()