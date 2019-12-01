def generate_squares(num: int):
    return dict((i, i**2) for i in range(1, num + 1))


print(generate_squares(5))
