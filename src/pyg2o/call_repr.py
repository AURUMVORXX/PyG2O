import inspect

def get_call_repr():
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name
    args_info = inspect.getargvalues(frame)
    
    args_str = []
    for arg in args_info.args:
        val = args_info.locals[arg]
        args_str.append(f"{val!r}" if not isinstance(val, str) else f"'{val}'")
    
    return f"{func_name}({', '.join(args_str)})"