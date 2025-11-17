#This problem will find which number is largest from the 3 given numbers
#This is the 4th day of 100 problems solving before 31st dec 2025

print("Enter the 3 numbers out of which you have to find which one if largest of them")

x = int(input("Enter the 1st number:- "))
y = int(input("Enter the 2nd number:- "))
z = int(input("Enter the 3rd numbers:- "))

if x > y > z :
    print("1st number is the greatest number")
elif y > x > z:
    print("2nd number is the greatest number")
else:
    print("3rd number is the greatest number")