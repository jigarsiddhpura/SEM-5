class CustomError(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

# Example of raising the custom error
try:
    raise CustomError("This is a custom error message")
except CustomError as ce:
    print(f"Caught an exception: {ce}")
