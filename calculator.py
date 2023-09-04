def calc(op, num1, num2):
    if op == 1:
        #Sum
        res = (num1 + num2)
        print(res)
    elif op == 2:
        #Multiplication
        res = (num1*num2)
        print(res)
    elif op == 3:
        #Subtraction
        res = (num1-num2)
        print(res)
    elif op == 4:
        #Division
        if num2 == 0:
            #Defense for division by zero
            print("Dividend cant be zero!")
        else:
            res = (num1/num2)
            print(res)
    elif op == 5:
        #Exponential
        num2 = int(num2)
        res = (num1**num2)
        print(res)
    else:
        #Defense for invalid option
        print("Invalid option")

print("Digit an option: 1-Sum 2-Multiplication 3-Subtraction 4-Division 5-Exponential\n")
opt = int(input())
#Will recieve user input and perform accordingly
print("Type the first value")
a = float(input())
print("Type the second value")
b = float(input())
calc(opt, a, b)