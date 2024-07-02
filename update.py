while True:
    input_string = input("Enter the calculation : ")
    number1, operator, number2 = input_string.split()

    # แปลง string เป็น float
    number1 = float(number1)
    number2 = float(number2)

    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 == 0:
            print("Cannot  by zero.")
            continue
        result = number1 / number2
    else:
        print("Invalid operator. Please enter a valid operator (+, -, *, /)")
        continue

    print(f"{number1} {operator} {number2} = {result}")

    next_calculator = input("You want to continue? (yes/no): ")

    if next_calculator.lower() == "no":
        break
