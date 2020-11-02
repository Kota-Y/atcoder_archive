def i_input(): return int(input())
def i_map(): return map(int, input().split())

def main():
    a, b = i_map()

    diff = abs(a-b)

    num10_1 = diff // 10
    num10_2 = num10_1 + 1

    diff1 = diff - 10 * num10_1
    diff2 = 10 * num10_2 - diff

    num5_1_1 = diff1 // 5
    num5_1_2 = num5_1_1 + 1
 
    num5_2_1 = diff2 // 5
    num5_2_2 = num5_2_1 + 1

    ans1 = num10_1 + num5_1_1 + diff1 - num5_1_1 * 5
    ans2 = num10_1 + num5_1_2 + num5_1_2 * 5 - diff1

    ans3 = num10_2 + num5_2_1 + diff2 - num5_2_1 * 5
    ans4 = num10_2 + num5_2_2 + num5_2_2 * 5 - diff2

    print(min(ans1, ans2, ans3, ans4))
    
if __name__ == '__main__':
    main()
