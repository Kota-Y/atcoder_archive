def s_input(): return input()

def main():
    x = s_input()
    S = s_input()

    for s in S:
        if s != x:
            print(s, end='')
    
    print()

if __name__ == '__main__':
    main()
