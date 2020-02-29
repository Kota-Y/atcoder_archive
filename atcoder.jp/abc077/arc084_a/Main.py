import bisect

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))

    ans = 0

    a_list.sort()
    c_list.sort()

    for i in range(n):
        toa_insert_index = bisect.bisect_left(a_list, b_list[i])
        toc_insert_index = bisect.bisect_right(c_list, b_list[i])
        ans += toa_insert_index * ( n - toc_insert_index )

    print(ans)

if __name__ == '__main__':
    main()