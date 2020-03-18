def main():
    n = int(input())
    
    ans = 0
    for i in range(n):
        if i == 0:
            l1 = 0
            l2 = 1
        elif i == 1:
            l1 = 2
            l2 = 1
        else:
            l1 = l2
            l2 = ans
        ans = l1 + l2

    print(ans)


if __name__ == '__main__':
    main()