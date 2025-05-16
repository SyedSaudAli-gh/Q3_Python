class Logger:
    def __init__(self, message):
        self.message = message
        print(f"{self.message} constructor")
        
    def __del__(self):
        print(f"{self.message} destructor")
        
log = Logger("Hello")
del log
print(log)