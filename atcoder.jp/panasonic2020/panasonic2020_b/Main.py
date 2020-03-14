def main():
    h, w = map(int, input().split())
    ans = 0
    if h == 1 or w == 1:
        print(1)
        exit()
    
    if h % 2 == 0:
        ans = h * w // 2
    else:
        if w % 2 == 0:
            ans = h * w // 2
        else:
            ans = h * w // 2 + 1 
    print(ans)

if __name__ == '__main__':
    main()
