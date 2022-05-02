def i_input(): return int(input())

def main():
    n = i_input()
    
    print('Blue' if n % 2 == 0 else 'Red')

if __name__ == '__main__':
    main()
