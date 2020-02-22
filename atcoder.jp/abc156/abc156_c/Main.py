inf = 1000000000

def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()

    ans = inf

    for i in range(1,101):
        tmp = 0
        for j in range(n):
            tmp += (num_list[j] - i) ** 2
        ans = min(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()