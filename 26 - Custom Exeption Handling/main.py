class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age

try: 
    user_age = int(input("Enter age: "))
    age = check_age(user_age)
except InvalidAgeError as e:
    print(e)
