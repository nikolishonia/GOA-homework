num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter one more number: "))

if num1 == num2 and num2 == num3 and num1 == num3:
    print("All three numbers are equal.")
elif num1 == num2:
    print("The first number is equal to the second.")
elif num1 == num3:
    print("The first number is equal to the third.")
elif num2 == num3:
    print("The second number is equal to the third.")
else:
    print("None of the numbers are equal.")


num4 = int(input("Enter a number from 1-12: "))
if num4 == 12 or num4 == 1 or num4 == 2:
    print("Winter")
elif num4 == 3 or num4 == 4 or num4 == 5:
    print("Spring")
elif num4 == 6 or num4 == 7 or num4 == 8:
    print("Summer")
elif num4 == 9 or num4 == 10 or num4 == 11:
    print("Autumn")


name = input("Enter your name: ")

if name == "admin":
    pw = input("Enter the password: ")
    if pw == "adminpassword123":
        print("სალამი ადმინ")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")