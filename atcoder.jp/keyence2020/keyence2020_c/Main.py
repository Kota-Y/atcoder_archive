def main():
    n, k, s = map(int, input().split())

    maxmax = s+1
    if maxmax == 10**9+1:
        maxmax = s-1

    ans_list = [maxmax]*n

    if k == 0:
        print(*ans_list)
        exit()

    if k == 1:
        ans_list[0] = s
        print(*ans_list)
        exit()

    if s == 1:
        for i in range(k):
            ans_list[i] = 1
        print(*ans_list)
        exit()

    if k != n:
        first = s // 2
        second = s - first
        for i in range(k):
            if i % 2 == 0:
                ans_list[i] = first
            else:
                ans_list[i] = second
        ans_list[n-1] = s
    else:
        for i in range(k):
            ans_list[i] = s       
        
    print(*ans_list)
 
if __name__ == '__main__':
    main()
