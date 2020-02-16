import math

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    print(math.ceil(n/min(a,b,c,d,e))+4)

if __name__ == '__main__':
    main()