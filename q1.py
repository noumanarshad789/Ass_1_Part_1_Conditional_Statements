# Part 1: Conditional Statements 

# 1.Write a program that checks if a given number is positive, negative, or zero.

num=int(input("enter a number: "))

if num>0:
    print("It is a positive number.")

elif num<0:
    print("It is a negative number.")

else:
    print("Your provided number is equal to zero")