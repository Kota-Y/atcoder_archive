def i_map(): return map(int, input().split())

def main():
    m1, d1 = i_map()
    m2, d2 = i_map()
    
    l = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    ans = 0
    if m1 == m2:
        ans += d2 - d1
    else:
        ans += d2
        ans += l[m1-1] - d1
        while m2 - m1 > 1:
            m1 += 1
            ans += l[m1-1]

    print(ans)

if __name__ == '__main__':
    main()
