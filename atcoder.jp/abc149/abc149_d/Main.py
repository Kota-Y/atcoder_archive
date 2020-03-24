def main():
    n, k = map(int, input().split())
    rs, ss, ps = map(int, input().split())
    s = input()

    score = 0

    winlose_list = [1] * n

    for i in range(n):
        if i-k >= 0 and s[i-k] == s[i] and winlose_list[i-k] == 1:
            winlose_list[i] = 0
            continue
            # if s[i] == 'r':
            #     score += rs
            # elif s[i] == 's':
            #     score += ss
            # elif s[i] == 'p':
            #     score += ps
            # winlose_list[i] = 0
            # print('aiko',i,s[i],score)
        else:
            if s[i] == 'r':
                score += ps
            elif s[i] == 's':
                score += rs
            elif s[i] == 'p':
                score += ss
            # print('Win',i,s[i],score)
            
    print(score)

if __name__ == '__main__':
    main()