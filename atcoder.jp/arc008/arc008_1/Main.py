def i_input(): return int(input())

def main():
    n = i_input()
    
    ans = float('inf')

    for i in range(6):
        for j in range(51):
            money = 100 * i + 15 * j
            num = 10 * i + j
            if num >= n:
                ans = min(ans, money)

    print(ans)

if __name__ == '__main__':
    main()
