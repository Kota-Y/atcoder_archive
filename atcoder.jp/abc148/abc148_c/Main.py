import fractions

def main():
    a, b = map(int, input().split())

    f=fractions.gcd(a,b)
    f2=a*b//f
    print(f2)

if __name__ == '__main__':
    main()
