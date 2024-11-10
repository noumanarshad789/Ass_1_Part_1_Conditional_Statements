# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

a=int(input("Enter a 1st side: "))
b=int(input("Enter a 2nd side: "))
c=int(input("Enter a 3rd side: "))

if a==b and b==c and c==a:
    print('It is an Equilateral triangle.')

elif a==b!=c or a!=b==c:
    print("It is an Isoscales triangle.")

elif a!=b!=c:
    print("It is an Scalene triangle.")