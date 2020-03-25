def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    ans = 0
    while(1):
        if num_list.count(0) == n:
            break
        i = 0
        while(i < n):
            if num_list[i] == 0:
                i += 1
            else:
                ans += 1
                while(i < n and num_list[i] != 0):
                    num_list[i] -= 1
                    i += 1

    print(ans)

if __name__ == '__main__':
    main()