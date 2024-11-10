# Write a program to determine if a given character is a vowel or consonant.

vowels="aeiou"

vowel_input=input("Enter a caharacter: ")

if vowel_input in vowels:
    print(f"{vowel_input} is a vowel.")

else:
    print(f"{vowel_input} is not a vowel.")
