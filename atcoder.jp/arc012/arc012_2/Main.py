def i_map(): return map(int, input().split())

def main():
    n, a, b, l = i_map()
    
    dist = a / b

    for _ in range(n):
        l /= dist

    print(l if l > 0.00000001 else 0)

if __name__ == '__main__':
    main()
