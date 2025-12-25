def run_in_times(count):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@run_in_times(count=5)
def print_text(text):
    print(text)


print_text('print me')
