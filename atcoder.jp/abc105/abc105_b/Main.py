def main():
    n = int(input())

    is_buy = False
    for i in range(n):
        if is_buy:
            break
        for j in range(n):
            if n == i * 4 + j * 7:
                is_buy = True
                break
    
    print('Yes' if is_buy else 'No')

if __name__ == '__main__':
    main()
