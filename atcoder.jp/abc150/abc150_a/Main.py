def main():
    K, X = map(int, input().split()) 

    if K * 500 >= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()