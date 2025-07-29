# 1)ლოგიკური ოპერატორებისა და შედარების ოპერატორებზე შეადგინეთ 10 მაგალითი,5 მაგალითმა უნდა დააბრუნოს False და 5 მაგალითმა უნდა დაააბრუნოს True

print(5 > 1 and 17 == 18)
print(14 > 80 or 31 < 3)
print(50 == 50 and 4 == 9)
print( 13 == 81 and 6 > 8)
print(90 > 99 or 37 == 2)
print(15 == 15 and 40 > 7)
print(111 > 88 or 95 == 22)
print(18 > 1 and 40 == 40)
print(11 > 3 or 80 == 16)
print(300 > 3 and 100 > 1)


# 2)კომენტარის სახით დაწერეთ თუ რა არის sequancing,iteration,selection აღწერე თითეული მათგანი თქვენი სიტყვებით

#sequencing aris tanmimdevroba, iteration aris gameoreba da selection aris archeva

# 3)მოიყვანე secuencing ის მაგალითი,და კომენტარით მიუწერე რატომ არის შენს მიერ მოყვანილი მაგალითი sequence

# sequencingis magaliti aris kodi, imitom rom kompiuteri kods kitxulobs zemodan qvevit

# 4)კომენტარის სახით ახსენით თუ რა არის for loop და რაში გვეხმარება ის

# for loop aris funqcia romelic gvexmareba kodis shemcirebashi da ragac monacemis bevrjer gamotanas

# 5)კომენტარის სახით ახსენით თუ რა გადაეცემა range() ფუნქციას და როგორ მუშაობს for loop

# ranges gadaecema ricxvi, da qvemot dawerili kodi shemdeg gameordeba magdenjer

# 6)შენი დავალებაა ტერმინალში გამოიყანო საყვარელი ავტომობილის სახელი ტერმინალში გამოიყენე for loop

for i in range(4):
    print("BMW")

# 7)შენი დავალებაა ტერმინალში გამოიტანო შენი გვარი 100 ჯერ

for i in range(100):
    print("Shonia")
  

# 8)შენი დავალებაა ტერმინალში გამოიტანო საყვარელი ფერი 46 ჯერ

for i in range(46):
    print("Purple")


# 9)შენი დავალებაა ტერმინალში გამოიტანო შენი სახელის პირველი ასო 32 ჯერ

for i in range(32):
    print("N")

# # გამეორება

# 10)მომხმარებელს შემოატანინე 3 სტრინგ ტიპის და ერთი ინტეჯერ ტიპის მნიშვნელობები და შენი დავალებაა მოახდინო ამ ოთხი მნიშვნელობის კონკატინაცია(გამოიყენე შესაბამისი ფუნქცია რომ მოახდინოთ მონაცემთა ტიპიების გარდაქმნა ერთ მონაცემთა ტიპში რომ შეძლოთ კონკატინაცია)

str1 = input("String 1: ")
str2 = input("String 2: ")
str3 = input("String 3: ")
intg = input("Integer: ")

print(str1 + str2 + str3 + intg)

# 11)შექმენი 4 ცვლადი,თითოეულში შეინახე განსხვავებული მონაცემთა ტიპები,შენი დავალებაა გაიგო ამ ცვლადებში შენახული მნიშვნელობის მონაცემთა ტიპი(გამოიყენე შესაბამისი ფუნქცია)

vr1 = "DBD"
vr2 = 13
vr3 = 1.88
vr4 = True

print(type(vr1))
print(type(vr2))
print(type(vr3))
print(type(vr4))

# 12)მომხმარებელს შემოატანინე 4 რიცხვი და ტერმინალში დააბრუნე ამ 4 რიცხვის ჯამი

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
num4 = int(input("Fourth number: "))

print(num1 + num2 + num3 + num4)
