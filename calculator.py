def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select option")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice = input(
        "You Choose Number(1/2/3/4)"
    )  # เป็นการแสดงตัวเลือกที่ผู้ใช้สามารถป้อนเพื่อเลือกการดำเนินการ#

    if choice not in ("1", "2", "3", "4"):
        print("You must select a number from the options.")
        continue

    try:
        number1 = float(input("Enter the first number"))
        number2 = float(input("Enter the Second Number"))

    except ValueError:
        print("You must Enter Number")
        continue

    if choice == "1":
        print(number1, "+", number2, "=", add(number1, number2))

    elif choice == "2":
        print(number1, "-", number2, "=", subtract(number1, number2))

    elif choice == "3":
        print(number1, "*", number2, "=", multiply(number1, number2))

    elif choice == "4":
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            print(number1, "/", number2, "=", divide(number1, number2))

    next_calculator = input("Yoy want to conitnue? (yes/no):")

    if next_calculator == "no":
        break
    else:
        print("Continue Enter The Number")
