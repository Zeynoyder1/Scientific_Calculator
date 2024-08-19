import cmath


def complex_calculator(final_result):
    while True:
        y = input("Enter an operation: ")
    
        if y.lower() == "stop":
            break

        if y.upper() == "AC":
            final_result = 0
            print(final_result)
            continue

        x = float(input("Enter a number: "))
    
        if y == "square":
            final_result += cmath.sqrt(x).real
        elif y == "log":
            final_result += cmath.log(x).real
        elif y == "cos":
            final_result += cmath.cos(x).real
        elif y == "sin":
            final_result += cmath.sin(x).real
        elif y == "tan":
            final_result += cmath.tan(x).real
        elif y == "cot":
            final_result += (1 / cmath.tan(x)).real
        elif y == "csc":
            final_result += (1 / cmath.sin(x)).real
        elif y == "sec":
            final_result += (1 / cmath.cos(x)).real
        elif y == "arc_cos":
            final_result += cmath.acos(x).real
        elif y == "arc_sin":
            final_result += cmath.asin(x).real
        elif y == "inverse_hcos":
            final_result += cmath.acosh(x).real
        elif y == "inverse_hsin":
            final_result += cmath.asinh(x).real
        else:
            print("Please enter a valid operation.")
            continue
        
        print(final_result)

    return final_result
