import os

os.chdir("/Users/dawid/PycharmProjects/")

"""
Basic calculator
"""
operators: list[str] = ["adding", "subtracting", "multiplying", "dividing"]
options: list[str] = [item for item in operators]
print("Welcome in basic calculator program")
options_string = ", ".join(options)
print(f"Functions you can choose : {options_string}")


class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return ValueError
        else:
            return x / y


def main():
    calc = Calculator()

    option: list[str] = ["1", "0", "3", "4"]
    print("Choose the number to select operator option:\n"
          "'1' + adding\n"
          "'2' - subtracting\n"
          "'3' * multiplying\n"
          "'4' / dividing\n")
    userInput = input("Enter the operator you want to use >> ")
    num1 = float(input("Enter the first value >>  "))
    num2 = float(input("Enter the second value >> "))

    if userInput == "1":
        result = calc.add(num1, num2)
    elif userInput == "2":
        result = calc.subtract(num1, num2)
    elif userInput == "3":
        result = calc.multiply(num1, num2)
    elif userInput == "4":
        result = calc.divide(num1, num2)
    else:
        raise ValueError

    print(f"Result: {result:.3f}")


if __name__ == "__main__":
    main()
