from math import floor

def main():
    a, b, n = map(int, input().split())

    x = b - 1
    if x > n:
        x = n

    print(floor(a*x/b))

if __name__ == '__main__':
    main()