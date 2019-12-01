def split_by_index(s, indexes):
    outp = []
    buff = ''
    for ind, elem in enumerate(s):
        if ind in indexes:
            outp.append(buff)
            buff = elem
        else:
            buff += elem
    if buff != '':
        outp.append(buff)
    return outp


if __name__ == '__main__':
    s = "pythoniscool,isn'tit?"
    indexes = [6, 8, 12, 13, 18]
    print(split_by_index(s, indexes))
