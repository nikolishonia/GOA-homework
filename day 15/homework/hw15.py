# 1)შექმენით ცვლადი სადაც შეინახავთ ინტეჯერ ტიპის მონაცემს,შემდეგ შეამოწმეთ თუ ეს რიცხვი რომელიც ცვლადში გაქვთ შენახული მეტია 10 ზე დაპრინტეთ "more than 10" სხვა შემთხვებაში დაპრინტეთ "less than 10"

num = 88

if num > 10:
    print("More than 10")
else:
    print("Less than 10")

# 2)მომხმარებელს შემოაყვანინეთ რიცხვი,შემდეგ შეამოწმეთ თუ ეს რიცხვი უდრის 15 ს დაუპრინტეთ "equal to 15" სხვა შემთხვევაში დაუპრინტეთ "not equal to 15"

num2 = int(input("Enter a number: "))

if num2 == 15:
    print("Equal to 15")
else:
    print("Not equal to 15")

# 3)მომხმარებელს შემოატანეთ სტრინგი შენი დავალებაა შეამოწმო,თუ მომხამრებლის მიერ შემოყვანილი სტრინგი არის giorgi დაუპრინტეთ 'you are correct" სხვა შემთხვევაში დაუპრინტეთ "you are wrong"

string = input("Enter a string: ")

if string == "giorgi":
    print("You are correct")
else:
    print("You are wrong")

# 4)დაატრიალეთ ფორ ციკლი 50 დან 100 მდე 5 ის გამოტოვებით

for i in range(50,100,5):
    print(i)

# 5)ფორ ციკლის დახმარებით გამოიტანეთ ტერმინალში თქვენი სახელი და გვარი

for i in range(1):
    print("Nicole Shonia")

# 6)while loop ის დახმარებით ტერმინალში გამოიტანეთ რიცხვები 20 დან 50 მდე

num3 = 20

while num3 < 50:
    print(num3)
    num3 = num3 + 1



