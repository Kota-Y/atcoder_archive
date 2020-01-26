def main():
    h, a = map(int, input().split())

    ans = 0

    while(h>0):
        h -= a
        ans +=1

    print(ans)

        
if __name__ == '__main__':
    main()