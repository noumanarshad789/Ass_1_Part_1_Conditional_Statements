# 20. Create a program that evaluates if an inputted number is prime.

num=int(input("Enter a number: "))

if num<=1:
    print(f"{num} is not a prime number.")

elif num>1 and num<=9:
    if num==2 or num==3 or num==5 or num==7:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

elif num>=10:
    if num%2==0 or num%3==0 or num%4==0 or num%5==0 or num%6==0 or num%7==0 or num%8==0 or num%9==0:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")

