# 1)მომხმარებელს შემოატანინეთ ორი რიცხვი,შეადარეთ ეს ორი რიცხვი ერთმანეთს(გამოიყენეთ შედარების ოპერატორები(>, <, ==)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print(num1 > num2)
print(num1 < num2) 
print(num1 == num2)


# 2)შექმენით 5 ცვლადი,3 ცვლადში შეინახეთ რიცხვები რომლებიც იქნებაინ სტრინგის ტიპის,დანარჩენ 2 ცვლადში შეინახეთ ჩვეულებრიბი ინტეჯერები,შენი დავალებაა იპოვო ამ ხუთი რიცხვის ნამრავლი,შემდეგ ეს ნამრავლი გაყავი რიცხვების რაოდენობაზე და დაპრინტე საბოლოო შედეგი,გამოიყენე შეაბამისი ფუნქცია რომ გადააქციო სტრინგი რიცხვები ინტეჯერად

num3 = "40"
num4 = "14"
num5 = "8"
num6 = 17
num7 = 11

num3 = int(num3)
num4 = int(num4)
num5 = int(num5)

num8 = num3 * num4 * num5 * num6 * num7
print(num8 / 4)


# 3)მომხმარებელს შემოატანინეთ სამი სტრინგ ტიპის მნიშვნელობა ასევე შემოატანინეთ ერთი ინტეჯერი,თქენი დავალებაა მომხმარებლის მიერ შემოყვანილ სამ სტრინგზე მოახდინოთ კონკატინაცია და შეინახოთ ცალკე ცვლადში ეს სამი გადაბმული სტრინგი,კონკატინაციის შემდეგ კი გაამრავლეთეს ეს მთლიანი სტრინგი მომხმარებლის მიერ შემოყვანილ რიცხვზე

str1 = input("First string: ")
str2 = input("Second string: ")
str3 = input("Third string: ")
num9 = input("Number: ")
num9 = int(num9)

cnctn = str1 + str2 + str3 
print(cnctn * num9)



# 4)კომენტარის სახით ახსენით თუ რომელი ლოგიკური ოპერატორები ვისწავლეთ და რომელი ოპერატორის დროს რას უფრო ენიჭება უპირატესობა(True , False) და რატომ

#chven viswavlet and da or operatorebi, and is dros false s eniweba upiratesoba, da or is dros trues, imitom rom and is dros orive piroba unda iyos shesrulebuli rom mivigot true, da or is dros mxolod ertia sawiro


# 5)გვერდით მიუწერეთ რას გამოიტანს შემეგი ოპერაციები

#      (and)                             (or)
# True and True -- True     |   True or True -- True       
# True and False -- False     |   True or False -- True
# False and True -- False   |   False or True -- True
# False and False -- False   |   False or False -- False 

# კომენტარის სახით მკიუწერეთ ასევე გვერდით თუ რატომ იქნება თქვენს მიერ შერჩეული პასუხი სწორი

# 6)მოიყვანე მაგალითები and და or ოპერატორებზე,დაპრინტე და გაუშვით ტერმინალში და ნახეთ შედეგი

print(False and True)
print(True or True)
print(False and False)
print(True and False)
print(False or True)

# გავლილი მასალა:
# 7)შექმენი 4 ცვლადი სადაც შეინახავთ სხვადასხვა მონაცემთა ტიპებს და შენი დავალებაა რომ გაიგო ამ ცვლადებში შენახული მონაცემების ტიპები(გამოიყენეთ შესაბამისი ფუნქცია)

vr1 = "Pick"
vr2 = 3
vr3 = 6.66
vr4 = False

print(type(vr1))
print(type(vr2))
print(type(vr3))
print(type(vr4))

# 8)მომხმარებელს შემოატანინე 3 მნიშნველობა,ერთის ტიპი იყოს float ერთის integer ერთის string და დაპრინტეთ ისინი(გამოიყენეთ შესაბამისი ფუნქციები რომ შემოყვანილ მნიშვნელობებს ქონდეთ შესაბამისი ტიპი(note:მომხმარებელს რომ შემოყავს მნიშვნელობა თავიდან ყოველთვის არის სტრინგი),თუ ფლოათს
#  შემოიყვანს მომხმარებელი გახადეთ ინფუთი ბულეან ტიპის თუ ინტეჯერს შემოიყვანს გახადეთ ინფუთი ინტეჯერ ტიპის

flt = input("Float: ")
intg = input("Integer: ")
str4 = input("String: ")
flt = bool(flt)
intg = int(intg)
print(flt)
print(intg)
print(str4)

