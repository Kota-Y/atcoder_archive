def main():
    n, x, y = map(int, input().split())

    x -= 1
    y -= 1

    ans_list = [0]*n

    for i in range(n):
        for j in range(i,n):
            ans_list[min(abs(i-j), abs(i-x)+abs(j-y)+1, abs(j-x)+abs(i-y)+1)] += 1

    for i in range(1,n):
        print(ans_list[i])

if __name__ == '__main__':
    main()