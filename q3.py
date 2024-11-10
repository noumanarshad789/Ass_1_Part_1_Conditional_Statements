# 3. Write a program that checks if a given year is a leap year.

num=int(input("Enter a year: "))

if num%4==0:
    print(f"Year {num} it is a leap year.")

else:
    print(f'Year {num} it is not a leap year.')