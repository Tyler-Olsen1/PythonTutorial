


try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
    print("Diveded by Zero")
except ValueError:
    print("Invalid input")
