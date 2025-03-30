import logging
from functools import wraps

logger = None

def set_default_logger(value: logging.Logger):
    """
    This function will the change default to your custom one.
    
    ## Declaration
    ```python
    def set_default_logger(value: logging.Logger):
    ```
    
    ## Parameters
    * `logging.Logger` **value**: custom logger object.
    """
    global logger
    logger = value

def handle_exception(func = None):
    """
    This decorator will handle all occuring exceptions and print them into the logger.
    
    ## Declaration
    ```python
    def handle_exception(func = None):
    ```
    
    ## Usage
    ```python
    from g2o import handle_exception
            
    @handle_exception
    def terrifying_function():
        print(5/0)
    
    @handle_exception    
    def check_pass_exception():
        wrong_position = {'x': 100, 'z': 300} # missing 'y'
        try:
            g2o.setPlayerPosition(0, wrong_position, pass_exception=True)   # exception will occur inside this function, but `pass_exception` will also raise it here
        except:
            print('Exception passed to the parent')
    ```
    """
    global logger
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            pass_exception = kwargs.pop('pass_exception', False)
            try:
                return f(*args, **kwargs)
            except Exception as e:
                if logger is not None:
                    logger.exception(e)
                else:
                    logging.exception(e)
                    
                if pass_exception:
                    raise
                
        return wrapper
    
    if func is not None:
        return decorator(func)
    
    return decorator