from fractions import gcd
from functools import reduce

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    n = int(input())
    num_list = [int(input()) for _ in range(n)]

    print(lcm_list(num_list))

if __name__ == '__main__':
    main()