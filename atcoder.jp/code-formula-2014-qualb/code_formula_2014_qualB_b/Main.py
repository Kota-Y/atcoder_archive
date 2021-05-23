def s_input(): return input()

def main():
    s = s_input()
    s = s[::-1]

    gusu = 0
    kisu = 0
    for i in range(len(s)):
        if i % 2 == 0:
            kisu += int(s[i])
        else:
            gusu += int(s[i])
    
    print(gusu, kisu)

if __name__ == '__main__':
    main()
