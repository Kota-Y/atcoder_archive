def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

def main():
    a, b = i_map()
    a_list = i_list()
    b_list = i_list()
    
    l = ['x'] * 10

    for i in range(a):
        l[a_list[i]-1] = '.'

    for i in range(b):
        l[b_list[i]-1] = 'o'

    print(*l[6:10])
    print(' ', end='')
    print(*l[3:6])
    print('  ', end='')
    print(*l[1:3])
    print('   ', end='')
    print(l[0])

if __name__ == '__main__':
    main()
