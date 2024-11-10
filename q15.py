# 15. Write a program to check if a number is within a specified range.

num=int(input("Enter a number: "))

if num in range (0,1000):
    print(f"{num} is in range of 0-1000.")

else:
    print(f"{num} is not in range of 0-1000.")
