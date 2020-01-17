def main():
    n = int(input())

    ans = 0

    for i in range(1,n+1):
        x = len(str(i))
        if x % 2 != 0:
            ans +=1

    print(ans)
    

if __name__ == '__main__':
    main()