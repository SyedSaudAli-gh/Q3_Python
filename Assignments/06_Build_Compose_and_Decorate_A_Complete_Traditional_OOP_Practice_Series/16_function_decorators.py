def log_function_call(func):
    def wapper():
        print("Function is being called")
        func()
    return wapper

@log_function_call
def say_hello():
    print("Say Hello!")
    
    
# log_function_call(say_hello)()
say_hello()