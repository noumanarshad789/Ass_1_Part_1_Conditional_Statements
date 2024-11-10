# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

marks=int(input("Enter your marks: "))

if marks>=90:
    print("A+")

elif marks<90 and marks>=85:
    print("A")

elif marks<85 and marks>=80:
    print("A-")

elif marks<80 and marks>=75:
    print("B+")

elif marks<75 and marks>=70:
    print("B")

elif marks<80 and marks>=75:
    print("B+")

elif marks<75 and marks>=70:
    print("B-")

elif marks<70 and marks>=65:
    print("C+")

elif marks<65 and marks>=60:
    print("C")

elif marks<60 and marks>=55:
    print("C-")

else:
    print("You are fail.")

