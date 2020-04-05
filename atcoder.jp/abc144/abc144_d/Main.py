import math

def main():
    a, b, x = map(int, input().split())

    if x > a * a * b * 0.5:
        theta = math.atan(2*(a*a*b-x)/(a*a*a))
    else:
        theta = math.atan(a*b*b/(2*x))

    print(theta*180/math.pi)

if __name__ == '__main__':
    main()