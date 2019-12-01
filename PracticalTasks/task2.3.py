def split_f(inp, sep=' '):
    outp = []
    buff = ''
    for i in inp + sep:
        if i == sep and buff == '':
            continue
        elif i == sep and buff != '':
            outp.append(buff)
            buff = ''
        else:
            buff += i
    return outp

print(split_f("welcome to the jungle"))
