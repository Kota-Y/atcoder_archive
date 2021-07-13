def i_input(): return int(input())

def main():
    n = i_input()

    for i in range(1, 200):
        if i * i * i == n:
            print('YES')
            exit()

    print('NO')

if __name__ == '__main__':
    main()
