def main():
    n, q = map(int, input().split())
    s = input()

    tmp = [0] * (n + 1)

    for i in range(1,n):
        tmp[i] = tmp[i-1] + ( 1 if s[i-1] ==  'A' and s[i] ==  'C' else 0 )
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(tmp[r-1] - tmp[l-1])

if __name__ == '__main__':
    main()