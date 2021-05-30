def s_input(): return input()

def main():
    s = s_input()

    if s == 'Sunday':
        print(0)
    elif s == 'Monday':
        print(5)
    elif s == 'Tuesday':
        print(4)
    elif s == 'Wednesday':
        print(3)
    elif s == 'Thursday':
        print(2)
    elif s == 'Friday':
        print(1)
    elif s == 'Saturday':
        print(0)

if __name__ == '__main__':
    main()
