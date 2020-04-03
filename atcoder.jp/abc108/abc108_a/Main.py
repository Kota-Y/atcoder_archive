def main():
    n = int(input())
    if n % 2 == 0:
        print(n//2*n//2)
    else:
        print((n-1)//2*(n-((n-1)//2)))

if __name__ == '__main__':
    main()