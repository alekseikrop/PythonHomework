import string

def most_common_words(filepath: str, number_of_words=3) -> list:
    inp_str = ''
    val = {}
    for line in open(filepath, 'r'):
        inp_str += line.translate(str.maketrans('', '', string.punctuation))
    inp_list = inp_str.split()

    for word in inp_list:
        if val.get(word.lower()) is None: val[word.lower()] = 1
        else: val[word.lower()] += 1
    output = sorted(list(val.items()), key=lambda x:x[1], reverse=True)
    return [i[0] for i in output][:number_of_words]


print(most_common_words(r'data/lorem_ipsum.txt'))
