def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    xa, ya, xb, yb, xc, yc = i_map()
    
    xb -= xa
    xc -= xa
    yb -= ya
    yc -= ya
    
    xa, ya = 0, 0

    print(abs(xb*yc-yb*xc)/2)

if __name__ == '__main__':
    main()
