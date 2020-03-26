from fractions import gcd    # 最大公約数: gcd(x, y)
from functools import reduce
def gcd_list(numbers):
    return reduce(gcd, numbers)

def main():
    n, x = map(int, input().split())
    num_list = list(map(int, input().split()))

    for i in range(n):
        num_list[i] = abs(num_list[i] - x)

    print(gcd_list(num_list))

if __name__ == '__main__':
    main()