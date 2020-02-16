import fractions

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

def main():
    n = int(input())
    num_list = list(map(int, input().split()))

    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for i in range(n):
        left[i + 1] = (fractions.gcd(left[i],num_list[i]))
        right[n - i - 1] = (fractions.gcd(right[n - i],num_list[n - 1 - i]))
    
    ans = 0
    for i in range(n):
        ans = max(ans,fractions.gcd(left[i],right[i + 1]))

    print(ans)

if __name__ == '__main__':
    main()