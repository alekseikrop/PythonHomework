def call_once(func):
    def call_once_wrapper(*args, **kwargs):
        if call_once_wrapper.calls == 0:
            outp = func(*args, **kwargs)
        else: outp = None
        call_once_wrapper.calls += 1
        return outp
    call_once_wrapper.calls = 0
    return call_once_wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
