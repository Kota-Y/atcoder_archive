def s_input(): return input()

def main():
    s = s_input()

    remove_s = 'aiueo'

    for tmp_s in s:
        if tmp_s in remove_s:
            continue
        print(tmp_s, end='')

    print()

if __name__ == '__main__':
    main()
