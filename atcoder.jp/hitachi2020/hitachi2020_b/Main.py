inf = 10 ** 19    # 1,000,000,000,000,000,000

def main():
    a, b, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    ans = inf

    for _ in range(m):
        x, y, c = map(int,input().split())
        tmp = a_list[x-1] + b_list[y-1] - c
        ans = min(ans, tmp)

    a_min = min(a_list)
    b_min = min(b_list)
        
    ans = min(ans, a_min+b_min)

    print(ans)


if __name__ == '__main__':
    main()