num1 = int(input("Enter 1st number:"))
num2 = int (input("Enter 2nd number:"))
ans = int(input("[1]add [2]modulo [3]multipy [4]divide: "))
if ans == 1:
    print("sum: ",num1 + num2)
elif ans == 2:
    print("remainder: ",num1 % num2)
elif ans == 3:
    print("product: ",num1 * num2)
elif ans == 4:
    print("quotient: ",num1 / num2)
