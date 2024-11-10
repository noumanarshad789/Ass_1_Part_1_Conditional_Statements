# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

age_input=int(input("Enter yoyr age: "))
if age_input<=17:
    print(f'{age_input} You are minnor.')

elif age_input>=18 and age_input<=64:
    print(f"{age_input} You are adult.")

else:
        print(f"{age_input} You are senior citizen.")