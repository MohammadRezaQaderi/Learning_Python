print('*' * 15)

name = input('what is your name? ')
print('hi ' + name)

courses = 'this is a beginner courses'
print(courses[1:-1])


course = 'Python for Beginners'
course = course.replace('o' , "4")
print(course)
print('x' in course)

print(10 / 3)
print(10 // 3)
print(10 ^ 3)


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


for x in range(4):
    for y in range(3):
        print(f'({x} , {y})')

numbers = [5 , 2 , 5 , 2 , 2]

for x in numbers:
    print('X' * x)

lists = [5 , 8 , 9 , 10 , 1 , 2 , 3]
Big = 0
for x in lists:
    if int(x) > int(Big):
        Big = x

print(Big)