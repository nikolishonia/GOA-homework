# 2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

sia = ["fkjdsh" , "gfdjsh" , "Fdkjs" , "FKJDHS" , "Gdskjh" , "Nslakdh"]
newsia = []

for i in sia:
    if i == i.lower() and i[0] == "g":
        newsia.append("Goga")
    elif i == i.upper() or i[0] == "N":
        newsia.append("Nika")
    else:
        newsia.append("ლიდერი")

print(newsia)

# 3)  შექმენით რიცხვებით სავსე სია, თუ რიცხვი არის ლუწი ან დგას ლუწ ინდექსზე, ჩაამატეთ მისი კვადრატი ახალ სიაში - გამოიყენეთ შესაბამისი მათემატიკური ოპერატორი, ხოლო თუ რიცხვი არის კენტი ან დგას კენტ ინდექსზე, ახალ სიაში ჩაამატეთ 2-ჯერ დიდი რიცხვი. გამოიყენეთ while ციკლი.

sia2 = [6 , 2 , 81 , 18 , 88 , 14 , 9]
newsia2 = []

i = 0

while i < len(sia2):
    if sia2[i] % 2 == 0 or i % 2 == 0:
        newsia2.append(sia2[i]**2)
    elif sia2[i] % 2 == 1 or i % 2 == 1:
        newsia2.append(sia2[i]*2)
    i = i + 1
        
print(newsia2)

# 4) შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ პატარა და ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, მაგალითად თუ მოცემული იქნება სიტყვა "Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.

sia3 = ["fdlksjf" , "LKFJD" , "fdlkj" , "cxbnmnxvb" , "pflkj" , "DJHFSL"]
newsia3 = []

for i in sia3:
    if len(i) > 6 or i == i.upper():
        newsia3.append(i.lower())
    else:
        newsia3.append(i+i)
        
print(newsia3)

# 5) მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას ამ სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. დაწერეთ ორივე ხერხით, for ციკლით და while ციკლით.

numbers = "0123456789"
newsia4 = []

for i in numbers:
    if numbers.index(i) % 2 == 0 or int(i) > 7:
        newsia4.append(int(i))
        
print(newsia4)

i = 0

while i < len(numbers):
    if i % 2 == 0 or int(numbers[i]) > 7:
        newsia4.append(int((numbers[i])))
    i = i + 1
    
print(newsia4)