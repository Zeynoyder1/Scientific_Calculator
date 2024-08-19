from math_calculator import math_calculator
from complex_calculator import complex_calculator
from stats_calculator import stats_calculator

def main():
    while True:
        final_result = 0 

        j = input("Enter a calculator name (cmath, math, stats, stop): ").lower()
        if j == "stop":
            break
        if j == "cmath":
            final_result = complex_calculator(final_result)
        elif j == "math":
            final_result = math_calculator(final_result)
        elif j == "stats":
            final_result = stats_calculator(final_result)
        else:
            print("Enter a valid calculator")

    print("Program ended.")
    print(final_result)

if __name__ == "__main__":
    main()
