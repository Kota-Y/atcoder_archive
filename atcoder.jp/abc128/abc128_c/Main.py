import itertools

def main():
    n, m = map(int, input().split())
    num_list = []
    for i in range(m):
        num_list.append(list(map(int,input().split())))

    p_list = list(map(int, input().split()))

    ans = 0

    for i in itertools.product([0,1], repeat=n):
        check = [0] * m
        for j in range(m):
            tmp = 0
            check[j] = True
            for n in range(1, num_list[j][0] + 1):
                if i[num_list[j][n] - 1] == 1:
                    tmp += 1
            if tmp % 2 != p_list[j] % 2:
                check[j] = False
        if all(check):
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()