import statistics

def stats_calculator(final_result):
    n = int(input("Enter number of elements: "))
    lst = list(map(int, input("Enter the numbers: ").strip().split()))[:n]
    print("List is - ", lst)

    while True:
        m = input("Enter an operation: ")
        
        if m.lower() == "stop":
            break

        if m == "harmonic_mean":
            final_result = statistics.harmonic_mean(lst)
        elif m == "median":
            final_result = statistics.median(lst)
        elif m == "mean":
            final_result = statistics.mean(lst)
        elif m == "high_median":
            final_result = statistics.median_high(lst)
        elif m == "low_median":
            final_result = statistics.median_low(lst)
        elif m == "mode":
            final_result = statistics.mode(lst)
        elif m == "standart_dev":
            final_result = statistics.stdev(lst)
        elif m == "variance":
            final_result = statistics.variance(lst)
        else:
            print("Please enter a valid operation.")
            continue
        
        print(final_result)

    return final_result
