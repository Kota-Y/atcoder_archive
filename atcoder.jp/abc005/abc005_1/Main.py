def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    a, b = i_map()
    
    print(b//a)

if __name__ == '__main__':
    main()
