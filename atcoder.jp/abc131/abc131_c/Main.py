from fractions import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

def main():
    a, b, c, d = map(int, input().split())

    ans = 0

    bc = b // c
    bd = b // d
    cd = lcm(c,d)
    bcd = b // cd

    bcount = b - bc -bd + bcd

    ac = (a-1) // c
    ad = (a-1) // d
    acd = (a-1) //cd

    acount = (a-1) - ac -ad + acd

    print(bcount-acount)

if __name__ == '__main__':
    main()