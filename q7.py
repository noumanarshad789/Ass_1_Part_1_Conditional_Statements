# 7. Write a program to find the largest of three numbers.

num_1=int(input("Enter a number_1: "))
num_2=int(input("Enter a number_2: "))
num_3=int(input("Enter a number_3: "))

if num_1>num_2 and num_1>num_3:
    print(f"{num_1} is greater than {num_2} and {num_3}.")

elif num_2>num_1 and num_2>num_3:
    print(f"{num_2} is greater than {num_1} and {num_3}.")

else:
    print(f"{num_3} is greater than {num_1} and {num_2}.")
      