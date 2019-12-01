import string

def test_1_1(*strings):
    outp = set()
    app = 0
    for i in string.ascii_lowercase:
        for j in strings:
             if i in j: app += 1
        if app == len(strings): outp.add(i)
        app = 0
    return outp


def test_1_2(*strings):
    outp = set()
    app = 0
    for i in string.ascii_lowercase:
        for j in strings:
             if i in j: app += 1
        if app >= 1: outp.add(i)
        app = 0
    return outp


def test_1_3(*strings):
    outp = set()
    app = 0
    for i in string.ascii_lowercase:
        for j in strings:
             if i in j: app += 1
        if app >= 2: outp.add(i)
        app = 0
    return outp


def test_1_4(*strings):
    outp = set()
    app = 0
    for i in string.ascii_lowercase:
        for j in strings:
             if i in j: app += 1
        if app == 0: outp.add(i)
        app = 0
    return outp


strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
print(test_1_2(*strings))
print(test_1_3(*strings))
print(test_1_4(*strings))
