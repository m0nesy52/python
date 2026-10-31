import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__
            args_str = f"args={args}" if args else ""
            kwargs_str = f"kwargs={kwargs}" if kwargs else ""
            
            all_args = []
            if args_str:
                all_args.append(args_str)
            if kwargs_str:
                all_args.append(kwargs_str)
                
            args_log = ", ".join(all_args) if all_args else "no args"
            log_line = f"[{current_time}] Function: {func_name} | Arguments: {args_log}\n"
            
            with open(filename, "a", encoding="utf-8") as f:
                f.write(log_line)
                
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_calls("function_logs.txt")
def example_function(a, b, c=3):
    return a + b + c

print("Выполняются вызовы функции...")
example_function(10, 20)
example_function(5, 5, c=10)

with open("function_logs.txt", "r", encoding="utf-8") as f:
    logs_content = f.read()

print("\nСодержимое файла логов после вызовов:")
print(logs_content)
