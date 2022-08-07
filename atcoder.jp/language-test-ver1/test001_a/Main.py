def i_input(): return int(input())

def main():
    n = i_input()
    num_list = list(input())
    
    ans = [0,0,0,0,0]
    
    for i in range(n):
        ans[int(num_list[i])] += 1
        
    print(max(ans), min(ans[1:]))

if __name__ == '__main__':
    main()
