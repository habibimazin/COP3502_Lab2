import math
print("Current Result: 0.0")

total_sum = 0.00
calculations = 0
showcalc = True
# calculator menu
while True:
    if showcalc == True:
        print("")
        print("Calculator Menu")
        print("---------------")
        print("0. Exit Program")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Logarithm")
        print("7. Display Average")
        print("")
    showcalc = True

    # operation performance

    operation = int(input("Enter Menu Selection: \n"))
    if 1 <= operation <= 6:
        first_Operand = float(input("Enter first operand:"))
        second_Operand = float(input("Enter second operand:"))

    if operation == 0:
        print("\nThanks for using this calculator. Goodbye! ")
        showcalc = False
        break

    elif operation == 1:
        add_value = first_Operand + second_Operand
        print("Current Result: " + str(add_value) + "\n")
        total_sum = total_sum + add_value
        calculations += 1

    elif operation == 2:
        sub_value = first_Operand - second_Operand
        print("Current Result: " + str(sub_value) + "\n")
        total_sum = total_sum + sub_value
        calculations += 1

    elif operation == 3:
        mult_value = first_Operand * second_Operand
        print("Current Result: " + str(mult_value) + "\n")
        total_sum = total_sum + mult_value
        calculations += 1

    elif operation == 4:
        div_value = first_Operand / second_Operand
        print("Current Result: " + str(div_value) + "\n")
        total_sum = total_sum + div_value
        calculations += 1

    elif operation == 5:
        exp_value = first_Operand ** second_Operand
        print("Current Result: " + str(exp_value) + "\n")
        total_sum = total_sum + exp_value
        calculations += 1

    elif operation == 6:
        log_value = math.log(second_Operand, first_Operand)
        print("Current Result: " + str(log_value) + "\n")
        total_sum = total_sum + log_value
        calculations += 1

    elif operation == 7:
        showcalc = False
        if calculations == 0:
            print("Error: No calculations yet to average! \n")
            continue

        average = (total_sum / calculations)
        print("Sum of calculations: " + str(total_sum))
        print("Number of calculations: " + str(calculations))
        print("Average of calculations: " + str(round(average, 2)))
        print("")

    else:
        showcalc = False
        print("Error: Invalid selection!")








