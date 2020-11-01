def swap_case(s):
    t = ''
    for i in s:
        if i.isupper() == True:
            t = t + i.lower()
        else:
            t = t + i.upper();
    return t

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result