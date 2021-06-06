def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    a, b, c = i_map()

    for i in range(1, 128):
        if i % 3 == a and i % 5 == b and i % 7 == c:
            print(i)

if __name__ == '__main__':
    main()
