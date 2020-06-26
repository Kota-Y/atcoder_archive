def i_input(): return int(input())

def main():
    n = i_input()
    ans_list = [i_input()]
    for j in range(n-1):
        w = i_input()
        for i, num in enumerate(ans_list):
            if num >= w:
                ans_list[i] = w
                break
        else:
            ans_list.append(w)
        ans_list.sort()

    print(len(ans_list))
 
if __name__ == '__main__':
    main()
