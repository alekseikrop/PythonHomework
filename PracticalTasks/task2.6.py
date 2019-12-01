def get_longest_word(s):
    spl = s.split()
    longest = spl[0]
    for i in spl:
        if len(i) > len(longest):
            longest = i
    return longest


if __name__ == '__main__':
    s = input('>')
    print(get_longest_word(s))
