import logging
def fun_call_decorator(func):
    def inner(*args, **kwargs):
        logging.debug("fun_call: %s" % (func.__name__))
        logging.debug("Arguments were: {}, {}".format(args[1:len(args)], kwargs))
        return func(*args, **kwargs)
    return inner
def fun_args_decorator(func):
    def inner(*args, **kwargs):
        logging.debug("Arguments were: {}, {}".format(args[1:len(args)], kwargs))
        return func(*args, **kwargs)
    return inner
def try_exept_IOError(func,n=3):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as e:
            logging.exception(str(func.__name__))

            raise
    return wrapper
