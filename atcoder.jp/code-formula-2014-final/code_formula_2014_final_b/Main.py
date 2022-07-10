def i_input(): return int(input())
def ceil(a, b): return (a + b - 1) // b

def main():
    n = i_input()

    kisu = ceil(n, 2)
    gusu = n // 2

    print(3*kisu-2*gusu)

if __name__ == '__main__':
    main()
