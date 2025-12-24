# 1) შექმენით რიცხვებით სავსე სია და ახალ სიაში ჩააგდეთ ყველა რიცხვი გამრავლებული 2-ზე. დაპრინტეთ ახალი სია.

sia = [55 , 80 , 41 , 2 , 3 , 19 , 11]
sia2 = []

for i in range(len(sia)):
    sia2.append(sia[i]*2)

print(sia2)

# 2) შექმენით სახელებით სავსე სია, მომხმარებელს შემოატანინეთ რაიმე რიცხვი, და ამ რიცხვის ინდექსზე ჩაამატეთ სახელი "ნიკა" თქვენს სიაში.

sia3 = ["gfjkg" , "dsfkjh" , "pfdksjh" , "cxmnbv" , "asdhgf"]

num = int(input("Enter a number: "))

sia3.insert(num , "nika")

print(sia3)

# 3) შექმენით string წინადადების ცვლადი, ამ წინადადებიდან დაპრინტეთ მხოლოდ ხმოვანი ასოები.

sent = "avtomobili modzraobda gadawarbebuli sichqarit"

for i in range(len(sent)):
    if sent[i] == "a" or sent[i] == "e" or sent[i] == "i" or sent[i] == "o" or sent[i] == "u":
        print(sent[i])

# 4) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 4-ზე მეტი სიგრძეში ან დგანან კენტ ინდექსზე. გამოიყენეთ remove() ფუნქცია.

sia4 = ["fdkgjh" , "pfkd" , "xmcnvb" , "qvck" , "pkjd" , "audsgf" , "qwriue" , "cvxvmnl"]

for i in sia4:
    if len(i) > 4 or sia4.index(i) % 2 == 1:
        sia4.remove(i)

print(sia4) 

# 5) შექმენით რიცხვებით სავსე სია, გამოითვალეთ რიცხვების საშუალო არითმეტიკული - რიცხვების ჯამი გაყოფილი რიცხვების რაოდენობაზე.

sia5 = [14 , 20 , 30 , 11 , 9 , 8 , 3]

print(len(sia5))

sia5 = sia5[0] + sia5[1] + sia5[2] + sia5[3] + sia5[4] + sia5[5] + sia5[6]

sia5 = sia5 / 7

print(sia5)