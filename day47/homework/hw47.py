# 1) შექმენით სახელებით სავსე სია და ასევე ცარიელი სია: Upper_name = [].  სახელების სიიდან ცარიელ სიაში ჩაამატეთ ყველა ის სახელი რომელიც იწყება დიდი ასოთი, გამოიყენეთ for ციკლი და შესაფერისი სიის და სტრინგის ფუნქციები.

sia = ["fdksjhf" , "Lfdskjf" , "Kfdsmdsk" , "Nvcxnbv" , "fhdshk" , "Zxcmvnb" , "pfdksjh"]

Upper_name = []

for i in range(len(sia)):
    if sia[i] == sia[i].capitalize():
        Upper_name.append(sia[i])

print(Upper_name)

# 2) შექმენით 2 სია - სახელების და გვარების. for ციკლის და ფუნქციების გამოყენებით სახელების სიაში ყველა სახელის ყველა ასო გახადეთ დიდი, ხოლო გვარების სიაში ყველა გვარის თითოეული ასო გახადეთ პატარა, სულ ბოლოს კი გააერთიანეთ სახელების სია გვარის სიასთან და დაპრინტეთ მიღებული შედეგი.


names = ["Jodi" , "Aileen" , "Lindsey" , "Eric" , "Morgan"]
surnames = ["Arias" , "Wuornos" , "Souvannarath" , "Harris" , "Geyser"]

namesup = ""
surlow = ""


for i in range(len(names)):
    namesup = names[i].upper()
    names[i] = namesup

for i in range(len(surnames)):
    surlow = surnames[i].lower()
    surnames[i] = surlow

print(names)
print(surnames)

names.extend(surnames)

print(names)

# 3) შექმენით სტრინგებით სავსე სია და ამ სიიდან ამოშალეთ ყველა ის სიტყვა რომელიც არის ან 6-ზე ნაკლები სიგრძეში, ან რომელიც მთავრდება დიდი ასოთი.

sia2 = ["fdksjhf" , "fdsmn" , "cxz" , "PfdjA" , "mnbxcS" , "odj" , "lkfjdlsj" , "triudX"]

for i in sia2:
    if len(i) < 6 or i[-1] == i[-1].upper():
        sia2.remove(i)

print(sia2)

# 4) შექმენით float მონაცემთა ტიპის ელემენტებით სავსე სია რომელშიც იქნება 10 float ელემენტი და ამ სიიდან ახალ ცარიელ სიაში ჩაამატეთ ის რიცხვები რომლებიც არიან 10-ზე მეტი და 100-ზე ნაკლები.

sia3 = [0.33 , 6.11 , 9.41 , 3.18 , 17.4 , 9.66 , 11.7 , 18.9 , 14.11 , 31.71]
sia4 = []

for i in range(len(sia3)):
    if sia3[i] > 10 and sia3[i] < 100:
        sia4.append(sia3[i])

print(sia4)

# 5) შექმენით 2 სია, პირველი სია იყოს სავსე 5 ცალი ქალაქის სახელებით, და მეორე სიაში მოთავსებული იყოს 10 ქვეყნის სახელი. თქვენი დავალებაა რომ ქვეყნის სახელებში ჩაამატოთ ყველა ქალაქის სახელები ცალ-ცალკე მენულე ინდექსიდან მეოთხე ინდექსის ჩათვლით. გამოიყენეთ for ციკლი და შესაბამისი ფუნქციები.

cities = ["Lubeck" , "Oslo" , "Irkutsk" , "Tbilisi" , "Liege"]
countries = ["North Korea" , "Russia" , "Norway" , "Germany" , "Mexico" , "Belgium" , "Georgia" , "Kyrgyzstan" , "Finland" , "Lebanon"]

for i in range(len(cities)):
    countries.insert(i , cities[i])

print(countries)