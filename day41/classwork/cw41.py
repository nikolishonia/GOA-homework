# 1)შექმენით სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიის ბოლოში დაამატე სიტყვა --> "ianvari" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

sia = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

sia.append("ianvari")

print(sia)

# 2)შექმენი სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიაში მეორე ინდექსზე დაამატე სიტყვა ---> "bati" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

sia2 = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

sia2.insert(2 , "bati")

print(sia2)

# 3)შექმენი სია ---->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე მე 5 ინდექსზე მდგომი ელემენტი და დაპრინტე საბოლოო სია ნახე ამოიშალა თუ არა

sia3 = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

sia3.pop(5)

print(sia3)

# 4)შექმენი სია --->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე True და ასევე ამოშალე "kote" და დაპრინტე საბოლოო სია და ნახე ამოიშალა თუ არა

sia4 = [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

sia4.remove(True)
sia4.remove("kote")

print(sia4)