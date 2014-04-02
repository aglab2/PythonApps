import logging

def LoggingDecorator(file):
    logging.basicConfig(filename=file,level=logging.DEBUG, format='(%(levelname)s) %(message)s')
    def decorator(f):
        def wrap(*args, **kwargs):
            logging.debug('%s - Started.  args:%s; %s', f.__name__, args, kwargs)
            retVal = f(*args, **kwargs)
            logging.debug('%s - Finished. args:%s; %s', f.__name__, args, kwargs)
            return retVal
        return wrap
    return decorator



@LoggingDecorator("log")
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

fact(9)