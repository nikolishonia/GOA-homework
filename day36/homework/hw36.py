# 1) შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
#    for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.

cities = ["Berlin" , "Lubeck" , "Irkutsk" , "Tbilisi" , "Oslo"]

for i in cities:
    if len(i) > 6:
        print(i)



# 2) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.

sia = ["sdkjfhksdjf" , "usncklfdvsur" , "pvksdkakv" , "ytawudfjssk" , "bncbskdjls" , "fghjkzxertsdmwitgfirpllcxzewrt"]

for i in sia:
    if len(i) % 15 == 0:
        print(i)

# 3) შექმენით სია რიცხვებით.  
# -> გამოიყენეთ for loop რათა დათვალოთ რამდენი რიცხვია სიაში.  
# -> არ გამოიყენოთ len() — დაითვალეთ ხელით.

sia2 = [88 , 1161 , 1412 , 646 , 90 , 16]

c = 0

for i in sia2:
    c = c + 1
print(c)

# 4) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.

sia3 = ["sdfhgsj" , "hhiln" , "pdsjhfs" , "astkj" , "aqwznbv"]

for i in sia3:
    if len(i) == 5:
        print(i)

# 5) მომხმარებელს შემოატანინე წინადადება.  
# -> გაიგე რამდენი სიმბოლოა წინადადებაში.  
# -> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.

sent = input("Enter a sentence: ")
print(len(sent))

a = 0

for i in sent:
    if (i) == "a" or (i) == "A":
        a = a + 1
print(a)

# 6) <= Boss Level =>
# შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
# --> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი

sia4 = ["qwpwzxkdl" , "zzxcxvczksdf" , "kkkhhvxczvsssdfcs" , "nnvbmclx" , "asdjhfls" , "plklkjsgd"]

ls = ""

for i in sia4:
    if len(i) > len(ls):
        ls = i

print(ls)
