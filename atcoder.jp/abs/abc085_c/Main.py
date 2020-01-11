def main():
    N, Y = map(int, input().split())
    
    num10000, num5000, num1000 = 0, 0, 0
    flag = False

    for i in range(N+1):
        for j in range(N+1-i):
            k = N - i - j
            total = 10000*i + 5000*j + 1000*k
            if total == Y and i+j+k == N :
                num10000, num5000, num1000 = i, j, k
                flag = True
                break

    if(not flag):
        num10000, num5000, num1000 = -1, -1, -1

    print('{} {} {}'.format(num10000, num5000, num1000))

if __name__ == '__main__':
    main()