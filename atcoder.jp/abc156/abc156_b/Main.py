import string
numbers = "0123456789"
alphabets = string.ascii_letters # a-z+A-Zをロード
characters = numbers + alphabets

def base_cvt(value, n=2):
    try:
        tmp = int(value)
    except:
        raise ValueError('Invalid value:', value)
 
    if n < 2 or n > len(characters):
        raise ValueError('Invalid n:', value)
 
    result = ''
    tmp = int(value)
    while tmp >= n:
        idx = tmp%n
        result = characters[idx] + result
        tmp = int(tmp / n)
    idx = tmp%n
    result = characters[idx] + result
    return result

def main():
    n, k = map(int, input().split())

    ans = len(base_cvt(n,k))
    
    print(ans)

if __name__ == '__main__':
    main()