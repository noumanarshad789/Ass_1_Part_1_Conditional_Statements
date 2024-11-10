# 14. Check if a year input by the user is a century year.

year_input=int(input("Enter an year: "))

if year_input%100==0:
    print(f"{year_input} is a century year.")

else:
    print(f"{year_input} is not a century year.")