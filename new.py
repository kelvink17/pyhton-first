
# students = ('Bola', 'tife', 'wariz')
# books = ['3', '9', '8']
# print(type(students))
# print(type(books))

# for num in range(16):
#     print(num)
import dataclasses
x= y= z =10.5

print(x)
print(y)
print(z)

















age =[2,4,6,8]
print(2 in age )


statement = '''rice is not nice'''

print(statement)

Department = 'Computer Science'
print(Department[9:16])

Course_title = 'Financial Analysis'
print(Course_title[0:10])

name = 'kelvink'
age = 20

print("my name is",name," i am",age,"year old")

name = 'ifeoluwa'
age = 25


print("my name is",name," i am celebrating my",age,"th birthday")





firstname = 'kelvink'
lastname = 'okorie' 
fullname = firstname + '\t' + lastname

print(fullname)

fruits = ['Apple','Pineapple','Orange','Banana']
print(fruits)


fruits.append('Grape')
print(fruits)

print(fruits[-5])

fruits2 = ['pawpaw','Cashew','Mango','Guava']
fruits.extend(fruits2)

print(fruits)

students = ['fawaz','frodd','mofe','eri','kingkelvin']
print(students) 
new_students = ['killerbean','jack frost']
students.extend(new_students)
print(students) 


genders = ['Male', 'Female','Mentally Unstable']
print(genders)
genders.append('Mentally derranged')
print(genders)
mentallysick = ['gay','lesbian']
genders.extend(mentallysick)
print(genders)
genders.remove('gay')
print(genders)
print(genders.pop(2))
genders.sort
print(genders)



students_id = {'id':[1,2,3,4,5],'Name':['fawaz','eri','musty','kelvin','mofe'],'Age':[12,10,19,20,13], 'Genders':['gay','female','female(bisexual)','male','gay(100%)']}
print(students_id['id'][3])
print(students_id.get('id'))
print(students_id.keys())
print(students_id.items())
student_id1 ={'id':[1,2,3],'name':['eri','kings','bola']}
print(student_id1.keys())
print(student_id1.items())
student_id1.update({'country':'Nigeria'})
print(student_id1)




# cut_off = 50
# fawaz_score = 79

# if fawaz_score >= 70:
#     print("Excellent (A)")
# elif fawaz_score >= 60:
#     print("Good (B)")
# elif fawaz_score >= cut_off:
#     print("Pass (C)")
# else:
#     print("Fail (F)")
# name = input("Enter your name: ").lower()
# score = int(input("Enter your score: "))

# if name == "fawaz":
    
#     print("Automatic Fail (F)")
# elif score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 70:
#     print("Excellent (A)")
# elif score >= 60:
#     print("Good (B)")
# elif score >= 50:
#     print("Pass (C)")
# else:
#     print("Fail (F)")
    
    


# parking_lot = ["lamborghini","bughatti","lexus","toyota","ford","ferrari","mercedes","Rolls-Royce","kia","hyundai","audi","bmw"]

# for i in parking_lot:
#       print(i)
# else:
#     print("The lot is empty")

    
#     #  Assignment 
    
    
    
    
    
    
    
# # Assignment

# # 1. Voting System
# age_input = int(input('Enter your age for the voting system: '))


# if age_input >= 18:
#     print('You are eligible to vote!')
# else:
#     print(f'You are not eligible to vote yet. You need {18 - age_input} more years.')

# # 2. Age Predictor
# current_age = int(input('Enter your current age for the age predictor: '))
# future_age = current_age + 5
# print(f'In the next 5 years, you will be {future_age} years old.')

# for i in range(15):
#      print(i)

# age_range = 25
# while age_range > 18:
#         print("fawaz is not eligble")
#         age_range -= 1


# for num in range(10):
#     if num ==5:
#         break
#     print(num)
# for num in range(10):
#         if num ==5:
#             continue
#         print(num)


# num1 = int(input("enter num1 :"))
# num2 = int(input("enter num2 :"))

# sum_num = num1 + num2
# print(f'sum is {sum_num}')

# tup = ("blue","red","green","white")
# print(tup[0])
# print(tup[3])

# students_id = {'id':[1,2,3,4,5],'Name':['fawaz','eri','musty','kelvin','mofe'],'Age':[12,10,19,20,13], 'Genders':['gay','female','female(bisexual)','male','gay(100%)']}
# for x in students_id:
#     print(students_id.keys())
#     print(students_id.values())




# day = int(input("what day is it: "))
# match day:
#     case 1:
#         print("sunday")
#     case 2:
#      print("monday")
#     case 3:
#      print("tuesday")
#     case 4:
#      print("wednesday")
#     case 5:
#      print("thursday")
#     case 6:
#      print("friday")
#     case 7:
#      print("saturday")    

# food_menu = int(input("pick number for food 1-6 : "))
# match food_menu:
#         case 1:
#             print(f"You picked number:{food_menu} which is 'chinease rice'")
#         case 2:
#              print(f"You picked number:{food_menu} which is 'beef soup'")
#         case 3:
#              print(f"You picked number:{food_menu} which is 'amala'")
#         case 4:
#             print(f"You picked number:{food_menu} which is 'ewedu'")
#         case 5:
#            print(f"You picked number:{food_menu} which is 'meat'")
#         case 6:
#            print(f"You picked number:{food_menu} which is 'meat soup'")                


days =  {
    "1: Sunday",
    "2: Monday",
    "3: Tuesday",
    "4: Wednesday",
    "5: Thursday",
    "6: Friday",
    "7: Saturday"
}
print(len(days))
days_inp = int(input("what day is it: "))

if days_inp > len(days):
     print("wrong input")
else:
    print(f" you picked {days.get(str(days_inp))}")
