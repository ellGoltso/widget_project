from functools import wraps


def log(filename = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"Start: {func.__name__} ok\n")
                else:
                    print(f"Start: {func.__name__} ok\n")

                result = func(*args, **kwargs)

                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"Finish: {func.__name__} ok\n")
                else:
                    print(f"Finish: {func.__name__} ok\n")

                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")

        return wrapper
    return decorator


