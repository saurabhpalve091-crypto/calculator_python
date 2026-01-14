number1 = float(input("Emter the First Number:"))
operator = input("Enter the Operator:")
number2 = float(input("Enter the Second Number:"))

if operator == "+":
    print("Answer is:", number1+number2)

elif operator == "-":
    print("Answer is:", number1-number2)

elif operator == "*":
    print("Answer is:", number1*number2)

elif operator == "/":
    print("Answer is:", number1/number2)

elif operator == "%":
    print("Answer is:", number1%number2)