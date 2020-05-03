def main():
    x = int(input())

    for a in range(0,500):
        for b in range(-500, 500):
            if a**5 - b**5 == x:
                print(a, b)
                exit()

if __name__ == '__main__':
    main()