import math

def dist(x,y,d):
    ret = 0.0
    for i in range(d):
        ret += pow(x[i] - y[i], 2)
    return pow(ret, 0.5)

def main():
    n, d = map(int, input().split())

    num_list = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    for i in range(n):
        for j in range(i+1,n):
            distance = dist(num_list[i],num_list[j],d)
            if math.ceil(distance) == math.floor(distance):
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
