# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

num=int(input("Enter a number: "))

if num%2==0 and num%3==0:
    print(f"{num} is divisible by 2 and 3.")

elif num%2==0:
    print(f"{num} is divisible by 2.")

elif num%3==0:
    print(f"{num} is divisible by 3.")