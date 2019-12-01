def count_letters(inp: str):
    outp = {}
    for i in inp:
        if outp.get(i) is None: outp[i] = 1
        else: outp[i] += 1
    return outp


print(count_letters('stringsample'))
