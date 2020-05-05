def main():
    s = input()

    len_s = len(s)

    match_list = ['.']

    if len_s >= 2:
        match_list.append('..')
    if len_s >= 3:
        match_list.append('...')

    for i in range(len_s):
        for j in range(1,len_s-i+1):
            if j > 3:
                continue
            tmp = s[i:i+j]
            match_list.append(tmp)
            if j == 2:
                match_list.append('.'+tmp[1])
                match_list.append(tmp[0]+'.')
            elif j == 3:
                match_list.append('.'+tmp[1]+tmp[2])
                match_list.append(tmp[0]+'.'+tmp[2])
                match_list.append(tmp[0]+tmp[1]+'.')
                match_list.append('..'+tmp[2])
                match_list.append(tmp[0]+'..')
                match_list.append('.'+tmp[1]+'.')

    print(len(set(match_list)))

if __name__ == '__main__':
    main()