def remember_result(func):
    def wrapper_remember_result(*args, **kwargs):
        wrapper_remember_result.last.append(func(*args, **kwargs))
        print(f'Last result = \
{wrapper_remember_result.last[wrapper_remember_result.count]}')
        wrapper_remember_result.count += 1
    wrapper_remember_result.count = 0
    wrapper_remember_result.last = [None, ]
    return wrapper_remember_result


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = {result}")
    return result


sum_list("a", "b")
sum_list("abc", "cde")
