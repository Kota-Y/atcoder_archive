from fractions import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)
def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    print(gcd_list(num_list))

if __name__ == '__main__':
    main()