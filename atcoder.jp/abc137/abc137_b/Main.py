def main():
    k,x = map(int, input().split())

    l = []
    
    for i in range(x-k+1,x+k):
        print(i, end=' ')

if __name__ == '__main__':
    main()