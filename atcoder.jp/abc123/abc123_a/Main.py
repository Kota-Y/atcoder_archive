def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    max_antena = max(a,b,c,d,e)
    min_antena = min(a,b,c,d,e)

    print('Yay!' if max_antena - min_antena <= k else ':(')

if __name__ == '__main__':
    main()