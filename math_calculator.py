import math

def math_calculator(final_result):
    while True:
        y = input("Enter an operation: ")
        
        if y.lower() == "stop":
            break

        if y.upper() == "AC":
            final_result = 0
            print(final_result)
            continue

        if y == "round_up":
            final_result = math.ceil(final_result)
        elif y == "round_down":
            final_result = math.floor(final_result)
        elif y == "rad_to_deg":
            x = float(input("Enter a number: "))
            final_result += math.degrees(x)
        elif y == "deg_to_rad":
            x = float(input("Enter a number: "))
            final_result += math.radians(x)
        elif y == "square":
            x = float(input("Enter a number: "))
            final_result += math.sqrt(x)
        elif y == "log":
            x = float(input("Enter a number: "))
            final_result += math.log(x)
        elif y == "cos":
            x = float(input("Enter a number: "))
            final_result += math.cos(x)
        elif y == "sin":
            x = float(input("Enter a number: "))
            final_result += math.sin(x)
        elif y == "tan":
            x = float(input("Enter a number: "))
            final_result += math.tan(x)
        elif y == "cot":
            x = float(input("Enter a number: "))
            final_result += 1 / math.tan(x)
        elif y == "csc":
            x = float(input("Enter a number: "))
            final_result += 1 / math.sin(x)
        elif y == "sec":
            x = float(input("Enter a number: "))
            final_result += 1 / math.cos(x)
        elif y == "arc_cos":
            x = float(input("Enter a number: "))
            final_result += math.acos(x)
        elif y == "arc_sin":
            x = float(input("Enter a number: "))
            final_result += math.asin(x)
        elif y == "inverse_hcos":
            x = float(input("Enter a number: "))
            final_result += math.acosh(x)
        elif y == "inverse_hsin":
            x = float(input("Enter a number: "))
            final_result += math.asinh(x)
        elif y == "abs":
            x = float(input("Enter a number: "))
            final_result += abs(x)
        elif y == "!":
            k = int(input("Enter a number: "))
            final_result += math.factorial(k)
        elif y == "**":
            z = float(input("Enter the exponent number: "))
            final_result = pow(final_result, z)
        elif y == "+":
            x = float(input("Enter a number: "))
            final_result += x
        elif y == "-":
            x = float(input("Enter a number: "))
            final_result -= x
        elif y == "*":
            x = float(input("Enter a number: "))
            final_result *= x
        elif y == "/":
            x = float(input("Enter a number: "))
            if x != 0:
                final_result /= x
            else:
                print("You can't divide a number by 0.")
                continue
        else:
            print("Please enter a valid operation.")
            continue
        
        print(final_result)

    return final_result


