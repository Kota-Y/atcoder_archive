import bisect

def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()

    ans = 0

    for i in range(n-2):
        for j in range(i+1,n-1):
            tmp = bisect.bisect_left(num_list, num_list[i]+num_list[j])
            ans += tmp - j - 1

    print(ans)

if __name__ == '__main__':
    main()