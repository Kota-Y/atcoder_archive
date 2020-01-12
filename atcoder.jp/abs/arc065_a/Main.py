import re

def main():
    s = input()
    s = re.sub('eraser', '', s)
    s = re.sub('erase', '', s)
    s = re.sub('dreamer', '', s)
    s = re.sub('dream', '', s)
    print('YES' if len(s) == 0 else 'NO')

if __name__ == '__main__':
    main()