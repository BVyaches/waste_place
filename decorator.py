def cache_args1(func):
    cache = {}
    def wrapper(*args, **kwargs):
        if str(args) + func.__name__ in cache:
            return cache[str(args) + func.__name__]
        else:
            result = func(*args, **kwargs)
            cache[str(args) + func.__name__] = result
            return result

    return wrapper


@cache_args1
def func(num):
    print(f'long {num}')
    return num ** 2


@cache_args1
def func2(a):
    print('Wait')
    return a // 2


print(func(2))
print(func(3))
print(func(2))
print()
print(func2(2))
print(func2(4))
print(func2(2))
