print ("Welcome")

Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))
Opn = input("Enter an operation (+,-,*,/): ")

# Operations
if Opn == '+':
    Ans = (Num1 + Num2)
    print (f"The Answer is: ", Ans)

elif Opn == '-':
    Ans = (Num1 - Num2)
    print (f"The Answer is: ", Ans)

elif Opn == '*':
    Ans = (Num1 * Num2)
    print (f"The Answer is: ", Ans)

elif Opn == '/':
    if Num2 !=0:
        Ans =(Num1 / Num2)
        print (f"The Answer is: ", Ans)
else:
    print("Error: Division by zero is not allowed.")
