def get_pairs(lst):
    outp = []
    for i, elem in enumerate(lst):
        if i == len(lst) - 1: break
        outp.append((elem, lst[i + 1]))
    return outp or None

if __name__ == '__main__':
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))
