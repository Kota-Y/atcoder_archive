import math

def main():
    a, b = input().split()

    x = a + b
    x = int(x)
    
    x = math.sqrt(x)

    if x.is_integer():
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()