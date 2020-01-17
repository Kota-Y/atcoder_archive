import math

def is_prime(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def main():
    x = int(input())
    
    ans = 0

    max = 10 ** 5

    for i in range(x,max+x):
        if is_prime(i):
            ans = i
            break

    print(ans)

if __name__ == '__main__':
    main()