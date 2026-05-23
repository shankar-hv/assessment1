# Word Frequency Counter

def frequency(s: str):
    copy = s.split()
    d = dict()
    new_copy = []
    for i in copy:
        new_copy.append(i.lower())
    for i in new_copy:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_val = 0
    for i in d:
        if d[i] > max_val:
            max_val = d[i]
            res = i
    return res       


def main()->None:
    inp = input('Enter the string: ')
     
    print(frequency(inp))

if __name__ == '__main__':
    main()