
# students = ('Bola', 'tife', 'wariz')
# books = ['3', '9', '8']
# print(type(students))
# print(type(books))

# for num in range(16):
#     print(num)
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

name = input("Enter your name: ").lower()
score = int(input("Enter your score: "))

if name == "fawaz":
    
    print("Automatic Fail (F)")
elif score < 0 or score > 100:
    print("Invalid score")
elif score >= 70:
    print("Excellent (A)")
elif score >= 60:
    print("Good (B)")
elif score >= 50:
    print("Pass (C)")
else:
    print("Fail (F)")
    
    
    
    #  Assignment 
    
    
    
    
    
    
    
# Assignment

# 1. Voting System
age_input = int(input('Enter your age for the voting system: '))

if age_input >= 18:
    print('You are eligible to vote!')
else:
    print(f'You are not eligible to vote yet. You need {18 - age_input} more years.')

# 2. Age Predictor
current_age = int(input('Enter your current age for the age predictor: '))
future_age = current_age + 5
print(f'In the next 5 years, you will be {future_age} years old.')
