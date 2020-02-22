mod = 1000000007

# 繰り返し二乗法  
def mod_pow(a, n, p):
    if n == 1:
        return a % p
    if n % 2 == 1:
        return (a* mod_pow(a, n - 1, p)) % p
    tmp = mod_pow(a, n / 2, p)
    return ( tmp * tmp ) % p

# 組み合わせ
def mod_cmb(n, k, p):
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    if (k > n - k):
        return mod_cmb(n, n - k, p)
    c = d = 1
    for i in range(k):
        c *= (n - i)
        d *= (k - i)
        c %= p
        d %= p
    return c * mod_pow(d, p - 2, p) % p

def main():
    n, a, b = map(int, input().split())

    ans = mod_pow(2, n, mod) - 1

    tmp_a = mod_cmb(n , a, mod)
    tmp_b = mod_cmb(n , b, mod)

    print((ans-tmp_a-tmp_b)%mod)

if __name__ == '__main__':
    main()