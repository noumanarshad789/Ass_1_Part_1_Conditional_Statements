# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

tem_input=int(input("Enter a temperature: "))

if tem_input<=0:
    print("It's a freezing temperature.")

elif tem_input>=1 and tem_input<=10:
    print("It's a cold temperature.")

elif tem_input>=11 and tem_input<=24:
    print("It's a Cool to Warm temperature.")

elif tem_input>=25 and tem_input<=35:
    print("It's a Hot temperature.")

else:
    print("It's a Very Hot temperature.")
