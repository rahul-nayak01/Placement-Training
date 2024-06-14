"""
try:

except ExcptionType1:
except ExcptionType2:
else:

finally:

"""
#zero div error and value error

try:
    num1=int(input("Enter a first number:"))
    num2=int(input("Enter a second number:"))
    result=num1/num2
    print("Result:",result)

except ValueError:
    print("Invalid input.Please enter a numeric values")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

else:
    print("No exception occured")

finally:
    print("End of program")