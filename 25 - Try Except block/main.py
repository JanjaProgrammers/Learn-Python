try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    qoutient = number1 / number2

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError as e:
    print(e)
    print("Only numbers are required as input")

except Exception:
    print("Something went wrong")

else:
    print(f"The quotient of {number1} and {number2} is {qoutient}")

finally:
    print("This line will execude regradless")