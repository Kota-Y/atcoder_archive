def main():
    n, a, b = map(int, input().split())
 
    train = n * a
    taxi = b
 
    print(min(train,taxi))
 
if __name__ == '__main__':
    main()