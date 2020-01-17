def main():
    a,b = map(int, input().split())
    
    x = a + b
    y = a - b
    z = a * b

    print(max(x,y,z))

if __name__ == '__main__':
    main()