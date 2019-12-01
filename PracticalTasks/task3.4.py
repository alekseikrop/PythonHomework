def combine_dicts(*args):
    fin_dict = {}
    for inp_dict in args:
        for key, value in inp_dict.items():
            if fin_dict.get(key) is None:
                fin_dict[key] = value
            else: fin_dict[key] += value
    return fin_dict


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
