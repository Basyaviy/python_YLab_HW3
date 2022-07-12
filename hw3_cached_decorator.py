def multiplier(number: int):
    return number * 2


def my_decorator(func):
    my_dict = {}

    def wrapper(*args, **kwargs):
        if len(args) == 1:
            result = func(*args, **kwargs)
            if args[0] in my_dict:
                print(f"{args[0]} - find in cache")
                return my_dict[args[0]]
            else:
                print(f"{args[0]} - is not in cache.. Add to cache")
                # Add new value in dict.
                my_dict.update({args[0]: result})

        else:
            result = -1
        return result
    return wrapper


my_result = my_decorator(multiplier)
print(my_result(5))
print(my_result(15))
print(my_result(5))
