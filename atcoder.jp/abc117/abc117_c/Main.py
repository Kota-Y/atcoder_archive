def main():
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    if m <= n:
        print(0)
        exit()

    num_list.sort()

    dist_list = []
    for i in range(1,m):
        dist_list.append(num_list[i]-num_list[i-1])

    dist_list.sort(reverse=True)


    ans = num_list[m-1]-num_list[0]
    for i in range(n-1):
        ans -= dist_list[i]

    print(ans)

if __name__ == '__main__':
    main()