import numpy as np
from scipy.linalg import lu

def linalg_calculator(final_result):
    n = int(input("Enter number of rows: "))
    s = int(input("Enter number of columns: "))
    arr = np.zeros([n,s], dtype = int)
    for i in range(n):
        for j in range(s):
            arr[i][j] = int(input(f"Enter the index({i+1},{j+1}): "))

    print("Matrix is - ", arr)
    while True:
        m = input("Enter an operation (det, inv, eigen, solve, ALU, frob, rank, lin_dep, AC, stop): ")
        
        if m.lower() == "stop":
            break

        if m.upper() == "AC":
            final_result = 0
            print(final_result)
            continue

        if m == "det":
            final_result = np.linalg.det(arr)
        elif m == "inv":
            final_result = np.linalg.inv(arr)
        elif m == "eigen":
             final_result = np.linalg.eig(arr)
        elif m == "solve":
            r = int(input("Enter number of rows: "))
            q = int(input("Enter number of columns: "))
            arr2 = np.zeros([r,q], dtype = int)
            for i in range(r):
                for j in range(q):
                    arr[i][j] = int(input(f"Enter the index({i+1},{j+1}): "))

            print("Matrix is - ", arr)
            try:
                final_result = np.linalg.solve(arr,arr2)
                print("answer: " ,final_result)

            except np.linalg.LinAlgError as e:
                print("matris is singular, there is no answer ",e)
        elif m == "ALU":
             P,L,U = lu(arr)
             print(f"P matrix is: {P}")
             print(f"L matrix is: {L}")
             print(f"U matrix is: {U}")
        elif m == "frob":
            final_result = np.linalg.norm(arr,'fro')
        elif m == "rank":
            final_result = np.linalg.matrix_rank(arr)
        elif m == "lin_dep":
            det_arr = np.linalg.det(arr)
            if det_arr == 0:
                print(det_arr)
                print("Linearly dependent")
            else :
                print(det_arr)
                print("Not linearly dependent")

        else:
            print("Please enter a valid operation.")
            continue
        print(final_result)

    return final_result