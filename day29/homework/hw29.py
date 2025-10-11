# # level 29
# 1)მოცემულია სტრინგი "PythonProgramming".
# ამოიღე პირველი 6 სიმბოლო და დაბეჭდე გამოიყენეთ slicing

st = "PythonProgramming"
print(st[0:7])

# 2)მოცემულია სია numbers = [10, 20, 30, 40, 50, 60, 70].
# ამოიღე მხოლოდ შუა 3 ელემენტი და დაბეჭდე გამოიყენეთ slicing (მინუს ინდექსებითაც)

numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:5])
print(numbers[-3:-5])

# 3)მოცემულია სტრინგი "HelloWorld".
# დაბეჭდეთ Hello ტერმინალში slicing ის გამოყენებით (მინუს ინდექსებითაც)

st2 = "HelloWorld"
print(st2[0:5])
print(st2[0:-5])

# 3)მოცემულია სია letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'].
# დაბეჭდე ყოველ პირველი მესამე მეხუთე ელემენტები გამოიყენეთ indexing (მინუს ინდექსებითაც)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0])
print(letters[2])
print(letters[4])

# 4)მოცემულია სტრინგი "Information".
# ამოიღე "forma" ნაწყვეტი slicing-ით (მინუს ინდექსებითაც)

st3 = "Information"
print(st3[2:7])
print(st3[-9:-4])

# 5)
# მოცემულია სტრინგი "abcdefghijklmno".
# შექმენი სამი სხვადასხვა სლაისი:

st4 = "abcdefghijklmno"


# პირველი შეიცავდეს მხოლოდ a დან d მდე ასოებს

# მეორე – შეიცავდეს j დან o მდე ასოებს

# მესამე – შეიცავდეს f დან j მდე ასოებს

print(st4[0:3])
print(st4[9:15])
print(st4[5:9])

