# import all file 
import converter

# import the method or class that we need
from converter import lbs_to_kg 

from utils import find_max
# Print in Phyton
print('*' * 15)

# Make Variable 
name = input('what is your name? ')
print('hi ' + name)

# Use String
courses = 'this is a beginner courses'
print(courses[1:-1])


course = 'Python for Beginners'
course = course.replace('o' , "4")
print(course)
print('x' in course)

print(10 / 3)
print(10 // 3)
print(10 ^ 3)


# Use If statement
is_hot = False
is_cold = True

if is_hot:
    print('''
        It is Hot Day!
        Drink Plenty of Water.
    ''')
elif is_cold:
    print('''
        It is cold Day!
        Wear Warm Clothes.
    ''')
else :
    print('It is Lovely Day')



# Use While
# Make Guess Game

secret_number = 9

Turn = 0
while Turn < 3:
    geuss = int(input("Guess : "))
    if secret_number == geuss:
        print('win')
        break
    Turn +=1
else:
    print('Sorry U Lose')

# Control Car with if and while

Massage_1 = ''
while Massage_1.upper() != 'QUIT':
    Massage_1 = input().lower()
    if Massage_1 == 'start':
        print('car strated')
    elif Massage_1 == "stop":
        print("'car stoped")
    elif Massage_1== "help":
        print('x')
    elif Massage_1 == 'quit':
        break
    else: 
        print('i dont understand')

# Nested For

for x in range(4):
    for y in range(3):
        print(f'({x} , {y})')

# Make F with X  with array

numbers = [5 , 2 , 5 , 2 , 2]
for x in numbers:
    print('X' * x)

# Find Big 

lists = [5 , 8 , 9 , 10 , 1 , 2 , 3]
Big = 0
for x in lists:
    if int(x) > int(Big):
        Big = x
print(Big)

# Make List Uniq

lists_1 = [1 , 5 , 4 , 7 , 5 , 6 , 1 , 1  , 2 , 1]
uniq = []
for x in lists_1:
    if x not in uniq:
        uniq.append(x)
print(uniq)

# Def the function

def square(number):
    return(number * number)

print(square(5))

# Class in python

class Point:
    #constructor
    def __init__(self , x , y):
        self.x = x
        self.y = y

   # method
    def move(self):
        print('move')
    def draw(self):
        print(f'draw {self.x}')

point1 = Point( 10 , 12 )
# make the atribute for point1 
point1.allah = 'allah'
print(point1.x)
point1.draw()

# Inheritance 

class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    # It means pass this line to interpreter
    pass

class Cat(Mammal):
    def be_annoying(self):
        print("ME U")

Mammal1 = Dog()
Mammal1.walk()


# use the imported file
print(converter.kg_to_lbs(50))

# use the imported method or class or ...
print(lbs_to_kg(450))


lists1 = [5 , 4 , 9 , 7 , 8 , 5 , 45 ,0 , 4]

print(find_max(lists1))