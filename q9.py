# 9. Take three sides of a triangle as input and check if they form a valid triangle.

a= int(input("Enter side 1: "))
b= int(input("Enter side 2: "))
c= int(input("Enter side 3: "))

if a+b>c or a+c>b or b+c>a:
    if a>0 and b>0 and c>0:
        print("These sides are of triangle.")
    
    else:
        print("These sides are not of triangle.")

else:
    print("These sides are not of triangle.")
