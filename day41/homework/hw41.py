# 1)კომენტარის სახით ჩამოწერე თითეული სიის ფუნქცია რაც ვისწავლეთ და მიუწერეთ გვერდით ახსნა განმარტება თუ რა გადაეცემა თითეულს და რას აკეთებს ის

# append - siis boloshi vamatebt elements, insert - siashi vamatebt elements indexis mixedvit, pop - siidan vashorebt elements indexis mixedvit, remove - siidan vashorebt elements tviton elementis saxelit

# 2)შექმენი რიცხვების სია.
# append() ფუნქციით დაამატე მასში რიცხვი 10 ბოლოში.
# დაბეჭდე სია რომ ნახო ჩაემატა თუ არა

numbers = [88, 13, 11, 60, 33]
numbers.append(10)
print(numbers)

# 3)შექმენი სახელების სია.
# append() ფუნქციით დაამატე შენი სახელი სიის ბოლოში
# დაბეჭდე სია.

names = ["eric" , "jodi" , "adam" , "aileen"]
names.append("Nicole")
print(names)

# 4)შექმენი სია სადაც შეიყვან სახელებს,შენიდავალებაა მომხმარებელს შემოატანინო რაიმე სახელი და შეინახო ცვლადში,შემდეგ ჩაამატე append()ის დახმარებით სიის ბოლოში მომხმარებლის შემოტანილი სიტყვა ~
# დაბეჭდე სია რომნახო ჩაემატა თუ არა

names2 = ["ksyusha" , "kirill" , "kev"]

usrinpt = input("Enter a name: ")

names2.append(usrinpt) 

print(names2)

# 5)შექმენი სია სადაც შეიყვანთ 5 სახეკს
# .insert() დახმარებით სიაში ჩაამატე მესამე ინდექსზე შენი სახელი

names3 = ["aileen" , "jodi" , "adam" , "ksyusha" , "kev"]
names3.insert(3 , "Nicole")
print(names3)

# 6)მომხმარებელს შემოატანინე სახელი და რიცხვი(integer 0 იდან 6 ჩათვლით)
# შენი დავალებაა შექმნა სია მინიმუმ 6 ელემენტიანი
# insert() დახმარებით დაამატე სიაში მომხმარებლის მიერ შემოტანილი რიცხვი,მომხმარებლის მიერ შემოტანილ ინდექსზე
# მაგ:მომხმარებელმა სახელი შემოიტანა საბა და რიცხვი 4 , შენი დავალებაა რომ საბა დაამატო მეოთხე ინდექსზე(გამოიყენე ცვლადის სახელები იმიტომ რომ არ იცი მომხმარებელი რა მნშვნელობებს შემოიტანს
# დაბეჭდე სია რომ ნახო ჩაემატა თუ არა

usr = input("Enter a name: ")
usr2 = int(input("Enter a number: "))

sia = ["sdfkjsh" , "pgfdlk" , "kxncvsm" , "qwtewewd" , "tbvnvndm" , "pcxcllxc"]
sia.insert(usr2 , usr)
print(sia)

# 7)შექმენი სია:

# fruits = ["apple", "banana"]

# insert() ფუნქციით ჩასვი "orange" 1 ინდექსზე.

fruits = ["apple", "banana"]
fruits.insert(1 , "orange")
print(fruits)

# 8)შექმენი სია:

# names = ["goga", "saba", "luka"]

# insert()-ით ჩასვი "irakli" ბოლოს წინა პოზიციაზე ანუ ლუკას წინ

names4 = ["goga", "saba", "luka"]
names4.insert(-1 , "irakli")
print(names4)

# 9)შექმენი სია:

# foods = ["bread", "milk", "cheese"]

# insert() ფუნქციით ჩასვი "water" სიის დასაწყისში.

foods = ["bread", "milk", "cheese"]
foods.insert(0 , "water")
print(foods)

# 10)შექმენი სია:numbers = [5, 10, 15]

# pop() ფუნქციით წაშალე ბოლო ელემენტი და დაბეჭდე განახლებული სია.

numbers2 = [5, 10, 15]
numbers2.pop(-1)
print(numbers2)

# 11)შექმენი სია:

# fruits = ["apple", "banana", "orange"]


# pop -ით ამოშალე "banana" და დაბეჭდე დარჩენილი სია.

fruits2 = ["apple", "banana", "orange"]
fruits2.pop(1)
print(fruits2)

# 12)შექმენი სია:

# names = ["goga", "saba", "luka"]


# ამოშალე "saba" pop()-ით  — შემდეგ დაბეჭდე სია რომ ნახო ამოიშალა თუ არა

names5 = ["goga", "saba", "luka"]
names5.pop(1)
print(names5)


# 13)შექმენი სია:

# colors = ["red", "green", "blue" , "yellow" , "black" , "purple"]


# pop()-ით წაშალე "red" და დაბეჭდე განახლებული სია.

# შემდეგ სიიდან ასევე ამოშალე yellow

# დაბეჭდე სია და ნახე შედეგი

colors = ["red", "green", "blue" , "yellow" , "black" , "purple"]
colors.pop(0)
print(colors)
colors.pop(2)
print(colors)

# 14)მომხმარებელს შემოტანინე რიცხვი(0 იდან 4 მდე და შეინახე ცვლადში

# შექმენი სია tems = ["pen", "pencil", "book", "eraser"] 

# pop ის დახმარებით სიიდან ამოშალე მომხმარებლის მიერ შემოტანილ რიცხვზე(ინდექსზე) მდგომი ელემენტი

usr3 = int(input("Enter a number from 0-4: "))

tems = ["pen", "pencil", "book", "eraser"]
tems.pop(usr3)
print(tems)

# 15)შექმენი სია:

# fruits = ["apple", "banana", "orange"]


# remove() ფუნქციით სიისდან წაშალე "banana".

# დაბეჭდე სია ნახე ამოიშალა თუ არა

fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)

# 16)შექმენი სია:

# nums = [3, 5, 3, 7]


# remove()-ით წაშალე 3 და დააკვირდი, მხოლოდ პირველი 3 იანი შაიშლება.

# დაბეჭდე სია რომ დარწმუნდე

nums = [3, 5, 3, 7]
nums.remove(3)
print(nums)

# 17)შექმენი სია:

# colors = ["red", "blue", "green"]


# remove() ფუნქციით წაშალე "blue" და დაბეჭდე განახლებული სია.

colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)

# 18)შექმენი სია:

# names = ["goga", "saba", "luka"]


# მომხმარებელს შემოატანინე ამ სამიდან რომელიმე სახელი შეინახე ცვლადში და remove()-ით წაშალე მომხმარებლის შემოტანილი სახელი სიიდან.

# დაბეჭდე სია რომ გაიგო მართლა ამოიშალა თუ არა

names = ["goga", "saba", "luka"]
usr = input("Enter one of the names listed above: ")
names.remove(usr)
print(names)

# 19)შექმენი სია:

# items = ["pen", "pencil", "book", "pencil"]


# remove()-ით წაშალე "pencil" და დაბეჭდე დარჩენილი სია.

items = ["pen", "pencil", "book", "pencil"]
items.remove("pencil")
print(items)
