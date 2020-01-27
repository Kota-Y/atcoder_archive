def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    ans = 0
    
    num_list.sort()

    left = num_list[int(n/2)-1] + 1
    right = num_list[int(n/2)]

    for i in range(left,right+1):
        ans += 1
            
    print(ans)

if __name__ == '__main__':
    main()