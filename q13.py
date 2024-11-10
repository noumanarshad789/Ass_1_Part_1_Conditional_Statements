# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
Operator_input=input("Enter Operator: ")

if Operator_input=="+":
    print(num1+num2)


elif Operator_input=="-":
    print(num1-num2)


elif Operator_input=="*":
    print(num1*num2)



elif Operator_input=="/":
    print(num1/num2)
