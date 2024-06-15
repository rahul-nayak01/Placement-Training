class MyCustomError(Exception):
    def __init__(self,message):
        self.message = message

try:
    raise MyCustomError("This is a custom error mesg.")
except MyCustomError as e:
    print("Custom error caught :",e.message)
    
