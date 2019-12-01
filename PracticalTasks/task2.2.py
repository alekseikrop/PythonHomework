def is_pal(word):
    forb = [',', '.', '-', ' ', '?', '!', '–', ':', ';']
    word_ed = ''.join(i.casefold() for i in word if not i in forb)
    return word_ed == word_ed[::-1]
