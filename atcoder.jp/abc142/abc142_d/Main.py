from collections import Counter

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    a, b = map(int, input().split())

    counter_a = Counter(prime_factorize(a))
    counter_b = Counter(prime_factorize(b))

    c_a = list(counter_a.keys())
    c_b = list(counter_b.keys())

    count = len(set(c_a) & set(c_b))

    print(count+1)

if __name__ == '__main__':
    main()