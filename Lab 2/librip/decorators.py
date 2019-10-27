def print_result(func):
    def decorated_func(*args):
        print(func.__name__)
        result = func(*args)
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for k, v in result.items():
                print(k, "=", v)
        else:
            print(result)
        return result

    return decorated_func
