def s_input(): return input()

def main():
    S = s_input()

    ans_s = ''
    before_s = 'a'
    for s in S:
        add_s = s
        if s != ' ':
            ans_s += add_s
            before_s = 'a'
            continue
        if before_s == 'a':
            add_s = ','
            ans_s += add_s
            before_s = 'i'
        
    print(ans_s)

if __name__ == '__main__':
    main()
