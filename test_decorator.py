def counter(func):
    count = {}

    count[func.__name__] = 0

    def wrapper(*args, **kwargs):
        count[func.__name__] += 1
        print(f'called {func.__name__} : {count[func.__name__]}')
        return func(*args, **kwargs)

    return wrapper


def dealer(func):
    def wrapper(*args, **kwargs):
        print('do')
        result = func(*args, **kwargs)
        print('done')
        return result

    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} вызвана с аргументами {args} {kwargs}')
        return func(*args, **kwargs)

    return wrapper


@counter
@dealer
def first():
    pass


first()
first()


@logger
@counter
def second(variable):
    pass


second('Параметр')
second(10)
second(12)
