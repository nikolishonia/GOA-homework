# 1) შექმენით სია რომელშიც იქნება მხოლოდ int მონაცემთა ტიპის ელემენტები, ამ სიიდან ამოშალე ყოველი რიცხვი რომელიც არის ლუწი ან დგას კენტ ინდექსზე სიაში, გამოიყენეთ remove() ფუნქცია და for ციკლი.

sia = [55, 43, 234, 90, 11, 48, 22]

for i in sia:
    if i % 2 == 0 or i.index() % 2 == 1:
        sia.remove(i)

print(sia)

# 2) შექმენით სია რომელშიც იქნება მხოლოდ სტრინგ მონაცემთა ტიპის ელემენტები, ამ სიის ბოლოში ცალ-ცალკე მეორედ ჩაამატე ყველა ის სიტყვა რაც უკვე არის ამ სიაში, გამოიყენეთ for ციკლი და სიის შესაბამისი ფუნქცია.

sia2 = ["dskjhf" , "ajdhfsl" , "pdkfhs" , "cvxjhd" , "pvcxdjkf"]

for i in sia2[:]:
    sia2.append(i)

print(sia2)

# 3) შექმენით 2 სია, ერთში იყოს მხოლოდ სტრინგ ტიპის ელემენტები, ხოლო მეორე სავსე იყოს ინტიჯერი მონაცემთა ტიპის ელემენტებით, რიცხვებით სავსე სიიდან, სტრინგებით სავსე სიაში ჩაამატე ის რიცხვები რომლებიც არიან 20-ზე მეტი და 50-ზე ნაკლები. გამოიყენეთ for ციკლი და შესაფერისი სიის ფუნქცია.

sia3 = ["fdskjg" , "asdkfjh" , "cxmnvb" , "pdfjkhs" , "ahdflfn"]
sia4 = [30 , 11 , 41 , 80 , 22 , 14 , 60 , 31]

for i in sia4:
    if i > 20 and i < 50:
        sia3.append(i)

print(sia3)

# 4) შექმენით სიტყვებით სავსე სია და ამ სიაში ყველა ისეთ სიტყვას რომელიც იწყება პატარა ასოთი, პირველი ასო გაუხადეთ დიდი. გამოიყენეთ for ციკლი და სტრინგის შესაბამისი ფუნქცია.

sia5 = ["fdslkfh" , "Gfdkj" , "cvcmnbx" , "Pfdsjd" , "nvcmxn" , "Kfdhjss"]
cap = ""

for i in range(len(sia5)):
    if sia5[i] != sia5[i].capitalize:
        cap = sia5[i].capitalize()
        sia5[i] = cap

print(sia5)

# 5) თქვენი სიტყვებით ახსენით რას აკეთებს გავლილი მასალიდან ყველა შესწავლილი სიის და სტრინგის ფუნქციები და for ციკლი.

# appendi amatebs siis bolos elements, inserti amatebs elements siashi indeqsis mixedvit
# remove-shi vwert romeli elementis amoshoreba gvinda siidan, pop-shi kide romeli elementis indeqss
# extend gamoiyeneba ori siis sheertebistvis
# index it vigebt elementis indeqss
# reverse atrialebs sias
# count aris imistvis rom gavigot ragac elementi siashi ramdenjer aris
# clear asuftavebs sias
# upper adidebs stringshi asoebs, lower apataravebs, da capitalize adidebs marto pirvel asos

