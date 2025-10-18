# 1)შექმენით სია -->  ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"] , თქვენი დავალებაა რომ პირველი 2 ელემენტი ჩაანაცვლოთ შემდეგი სიით --> ["irina" , "milana" , "kira", "mate"] //////////////// და ასევე სიის ბოლო ორი ელემენტი შეანაცვლე შემდეგი სიით --> ["gia" , "emzari" , "xvicha"] ამის შემდეგ დაპრინტეთ საბოლოო სია

sia = ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"]

sia[0:2] = ["irina" , "milana" , "kira", "mate"]

sia[4:6] = ["gia" , "emzari" , "xvicha"]

print(sia)



# 2)შექმენით ცვლადი და მომხმარებელს შემოატანინეთ რიცხვი,თუ რიცხვი ლუწია დაუპრინტეთ "EVEN" შემდეგ შეამოწმეთ თუ რიცხცვი არის კენტი დაუპრინტეთ "Odd"

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
elif num % 2 == 1:
    print("Odd")

    