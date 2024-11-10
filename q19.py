# 19. Check if a string input is uppercase, lowercase, or a mix.

str_input = input("Enter a string: ")

if str_input.isupper():
    print("The string is in uppercase.")
elif str_input.islower():
    print("The string is in lowercase.")
else:
    print("The string is a mix of uppercase and lowercase.")
