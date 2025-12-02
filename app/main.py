from typing import Callable


def cache(func: Callable) -> Callable:
    args_set = {}

    def decorator(*args) -> Callable:
        for key, arg in args_set.items():
            if key == args:
                print("Getting from cache")
                return arg
        print("Calculating new result")
        result_of_operation = func(*args)
        args_set[args] = result_of_operation
        return result_of_operation

    return decorator
