def main():
    l,r = map(int, input().split())
    
    ans = 10**8

    if r - l + 1 >= 2019:
        print(0)
        exit()

    for i in range(l,r):
        for j in range(i+1,r+1):
            tmp = (i*j) % 2019
            ans = min(ans, tmp)
            if ans == 0:
                break
        if ans == 0:
            break

    print(ans)
        
if __name__ == '__main__':
    main()