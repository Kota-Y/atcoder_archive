import math

def main():
    a,b = map(int, input().split())

    avg = (a + b) / 2

    print(math.ceil(avg))

if __name__ == '__main__':
    main()