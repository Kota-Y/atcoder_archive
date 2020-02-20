def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

def main():
    n = int(input())

    ans = 0

    for i in range(1,n+1):
        if i % 2 == 0:
            continue
        if len(make_divisors(i)) == 8:
            ans += 1
        
    print(ans)

if __name__ == '__main__':
    main()