import math

def main():
    a, b = map(int, input().split())

    for i in range(1,1001):
        if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
            print(i)
            exit()

    print(-1)

if __name__ == '__main__':
    main()