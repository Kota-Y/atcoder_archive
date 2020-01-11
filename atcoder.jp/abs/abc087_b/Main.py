def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    
    count = 0

    for yen500 in range(A+1):
        for yen100 in range(B+1):
            for yen50 in range(C+1):
                total = 500 * yen500 + 100 * yen100 + 50 * yen50
                if X == total:
                    count += 1
                total = 0

    print(count)

if __name__ == '__main__':
    main()