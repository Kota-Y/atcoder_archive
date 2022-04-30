from collections import Counter
def i_input(): return int(input())
def s_input(): return input()

def main():
    n = i_input()
    s = s_input()

    l = []
    for i in range(n):
        l.append(s[i])
    co = Counter(l)

    ans_max = max(co['1'], co['2'], co['3'], co['4'])
    ans_min = min(co['1'], co['2'], co['3'], co['4'])
    
    print(ans_max, ans_min)

if __name__ == '__main__':
    main()
