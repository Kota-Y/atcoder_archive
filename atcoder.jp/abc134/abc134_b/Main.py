import math

def main():
    n, d = map(int, input().split())

    one = 1 + 2 * d

    print(math.ceil(n/one))

if __name__ == '__main__':
    main()
