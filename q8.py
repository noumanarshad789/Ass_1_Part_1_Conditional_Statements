# 8. Create a program that checks if a given string is a palindrome.

inter_str=input("Enter a string: ")
reverse_str=inter_str[::-1]

# print(reverse_str)

if inter_str==reverse_str:
    print("It is Palindrome.")

else:
    print("It is not a Palindrome.")
