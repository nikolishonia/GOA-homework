# 2) კომენტარების სახით თავიდან ახსენით რა არის conditional statement, რა დანიშუნლება გააჩნიათ და როგორი სახის განცხადებები გვაქვს.

#conditional statement aris pirobiti gancxadebebi da gvaqvs if da else gancxadebebi

# 3) for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ. 

for i in range(50):
    print("hello world")

# 4) while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.

num = 3

while num < 18:
    print(num)
    num = num + 1


# 5) მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში. შექმენით პირობა თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect".


password = input("Enter password:")

if password == "1234":
    print("Password is correct")
else:
    print("Password is incorrect")



# 6) შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას. თუ სახეობა უდრის "ძაღლი" დაბეჭდეთ "woaf! woaf!", სხვა შემთხვევაში "შენ არ გყავს ძაღლი"

animal = input("Enter an animal:")

if animal == "dog":
    print("Woof! Woof!")
else:
    print("You do not have a dog.")


# 7) უყურეთ შემდეგ ვიდეო წყაროსს:

# -- https://youtu.be/FvMPfrgGeKs --