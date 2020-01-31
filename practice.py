# a = int(input('enter number: '))
# b = 5
# if a > b:
#     print("This is right.")
# else:
#     print("This is not right.")

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# guess_car = input('Enter car model: ')
# cars = ['audi', 'bmw', 'subaru', 'toyota', 'tesla', 'lexus']
# if guess_car == 'tesla':
#     print(f"{guess_car} is a electric vehicle.")
# elif guess_car == 'lexus':
#     print(f"{guess_car} is a hybrid car.")
# elif guess_car not in cars:
#     print(f"{guess_car} is not a vehicle.")
# else:
#     print(f"{guess_car} is a gasoline vehile.")

# banned_users = ['maria','nicole', 'anna', 'sofia']
# user = input("Enter your name: ")
# if user not in banned_users:
#     print(user.title()+", you can post a response if you wish.")
# else:
#     print(user.title()+", your are banned user. You can't post.")

# requested_topping = 'mashroom'
# if requested_topping != 'pepporoni':
#     print("here is only pepporoni.")


# age = 19
# if age >= 18:
#     print(f"{age}, you can vote.")
# else:
#     print(f"{age}, you are too old to vote.")


# fruits = ['apple','grapes','bananas','peach','apricot']
# fav_fruit = fruits[2:]
# print(fav_fruit)

# age = int(input("Enter your age: "))

# if age < 4:
#     print("Your admission cost is $0")
# elif age < 18:
#     print("Your admission cost is $5")
# else:
#     print("Your admission cost is $10")

# age = int(input("Enter your age: "))
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 65:
#     price = 10
# elif age >= 70:
#     price = 1

# print("Your admission cost is $"+str(price)+".")


# order_pizza = str(input("Enter your toppings: "))
# store = ['pepporoni','mashrooms','vegan', 'onion','green pepper']
# if order_pizza in store:
#     print(f"I am adding {order_pizza}.")
# else:
#     print(f"Sorry, {order_pizza} we dont have it.")

# print("\nYour pizza is ready.")

# alien_color = ['green','yellow','red']
# if alien_color == 'green':
#     print("Your earned just 5 points")
# elif alien_color != 'green':
#     print("Your are failed.")

# color = 'green', 'red'
# if color != 'green':
#     print("Your are earned 5 points.")
# elif color == 'red':
#     print("You earned 10 points.")

# colors = ['green', 'white', 'red']
# if 'green' in colors:
#     print("Player earned 5 points.")
# elif 'yellow' not in colors:
#     print("Player earned 10 points.")
# elif 'red' in colors:
#     print("Player earned 15 points.")

# import sys
# import random

# ans = True

# while ans:
#     question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
#     answers = random.randint(1,8)
    
#     if question == "":
#         sys.exit()
    
#     elif answers == 1:
#         print ("It is certain")
    
#     elif answers == 2:
#         print ("Outlook good")
    
#     elif answers == 3:
#         print ("You may rely on it")
    
#     elif answers == 4:
#         print ("Ask again later")
    
#     elif answers == 5:
#         print ("Concentrate and ask again")
    
#     elif answers == 6:
#         print ("Reply hazy, try again")
    
#     elif answers == 7:
#         print ("My reply is no")
    
#     elif answers == 8:
#         print ("My sources say no")

# username = input("Login: >> ")

# #list of allowed users
# user1 = "Jack"
# user2 = "Jill"

# #control that the user belongs to the list of allowed users
# if username == user1:
#     print("Access granted")
# elif username == user2:
#     print("Welcome to the system")
# else:
#     print("Access denied")

# num1 = int(input("Enter 1 num: "))
# num2 = int(input("Enter 2 num: "))
# num3 = int(input("Enter 3 num: "))
# average = (num1+num2+num3)/3
# print(f"Your average is {average}.")

# person = ['ben', 'ted', 'tom']
# for x in person:
#     if x == 'ben':
#         print(x.title())
#     else:
#         print("not here")

# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# area = length * width
# print("The area is: ", area)


# for x in range(4):
#     if (x==2):
#         continue
#     print(x)

# number = (1,2,3,4,5,6,7,8,9,10)
# num_sum = 0
# count = 0
# for x in number:
#     num_sum = num_sum + x
#     count = count + 1
#     print(count)
#     if count == 8:
#         break

# a = [1,2,3,4,5,6]
# del a[4]
# print(a)

# L = ['yellow', 'green', 'red', 'white', 'black']
# L.append('blue')
# L.insert(5,'orage')
# print(sorted(L))
# L.reverse()
# print(L)

# x = [i for i in range(10)]
# print(x)

# for i in range(10):
#     print(i)

# square = []
# for i in range(10):
#     square.append(i**2)
#     if i == 5:
#         break
#     print(square)
#     if i > 5:
#         continue
#     print(square)

# list1=[1,2,3,4,5,6,7,8,9,10]
# multiplied = [item*50 for item in list1]
# print(multiplied)


# import random

# while True:

#     val = random.randint(1, 30)
#     print(val, end=" ")

#     if val == 2:
#         break

# print()

num = 0

# while num < 11:

#       num = num + 1

#       if num % 2 == 0:
#          continue

#       print(num, end=" ")


# lyrics = """\
# Are you really here or am I dreaming
# I can't tell dreams from truth
# for it's been so long since I have seen you
# I can hardly remember your face anymore
# """


# for i in lyrics:

#     print(i, end=" ")

# name = input("Enter name: ")

# if (name == "Robert" or name == "Frank" or name == "Jack"
#       or name == "George" or name == "Luke"):
#     print("This is a male")
# else:
#     print("This is a woman")

# table = 2
# start = 1
# max = 10 
# print("-"*20)
# print("The table of 2")
# print("-"*20)
# i = start
# while i <= max:
#     result = i * table
#     print(i,"*", table, "=", result)
#     i = i+1
# print("-"*20)
# print("Done counting...")
# print("-"*20)

# def name():
#     name = input("enter your name: ")
#     return name
# print(name())


# name = "Inomjon Pochoev"
# for i in name[::-1]:
#     print(i)
# print("".join(reversed(name)))
# print(name[::1])

# months = {1:"Janurary",2:"February", 3:"March",4:"April",5:"May", 6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# for key in months:
#    print(key)

# sentence = "I am learning python. Because I want to be python developer."
# print(sentence.split())

# print("+---"*5)
# print("Inomjon Pochoev".split())
# print("+---"*5)

# name = input("Give me your name: ")
# print("Your name is: "+ name)

# i = 0
# while i < 10:
#     print(i)
#     i = i+1

# while True:
#     print("Hello")
#     if print == 5:
#         break

# import sys, pygame
# pygame.init()

# size = width, height = 320, 240
# speed = [2, 2]
# black = 0, 0, 0

# screen = pygame.display.set_mode(size)

# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]

#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()

# age = int(input("Enter your age: "))
# if age > 17:
#     print("You can see R rated movies.")
# elif age <17 and age > 12:
#     print("You can see PG-13 rated movies.")
# else:
#     print("You can see only PG rated movies. ")

# count = 0
# while(count < 9):
#     print("this is ", count)
#     count = count +1
# print("Good bye")

# var = 1
# while var == 1:
#     num = input("Enter a number: ")
#     print("You entered "+ num)
# print("Good bye")

# count = 1
# while count <5:
#     print(count, " is less then 5")
#     count = count + 1
# else:
#     print(count, " is not less than 5")

# list_of_students = ["Michele", "Sara", "Cassie"]

# name = input("Type name to check: ")
# if name in list_of_students:
#     print("This student is enrolled.")
# else:
#     print("You are not enrolled.")


# while True: 
#     usr_command = input("Enter your number: ")
#     if usr_command == "5":
#         print("your are guessed " + usr_command)
#     else: 
#         print("Your are not quessed " + usr_command)

# import random
# a = random.randint(2,6)
# print(a)

# def get_integer():
#     return int(input("Give me a number: "))
# age = get_integer()
# school_year = get_integer()
# if age > 15:
#     print("You are over the age of 15")
# print("You are in grade " + str(school_year))

 
# def fibonacci():
#     num = int(input("enter number: "))
#     i = 1
#     if num == 0:
#         fib = []
#     elif num ==1:
#         fib = [1]
#     elif num ==2:
#         fib = [1,1]
#     elif num > 2:
#         fib = [1,1]
#         while i < (num - 1):
#             fib.append(fib[i]+fib[i-1])
#             i += 1
#     return fib
# print(fibonacci())
# input()        
        
        
        
# name = set()
# name.add("Inomjon")
# name.add('Akbar')
# name.add("nodir")
# print(name)
# names = ["Akbar", "nodir", "farhod"]

# names.reverse()
# print(names)

# import random
# s= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 8
# p = ("".join(random.sample(s,passlen)))
# print(p)

# def square(num):
#     return num * num

# user_num = input("Give me a number: ")
# print(square(num))

# price = 100000
# has_good_credit = input(False)

# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: {down_payment}")

# import random

# guesses_made = 0

# name = input('Hello! What is your name?\n')

# number = random.randint(1, 20)
# print ('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

# while guesses_made < 6:

#     guess = int(input('Take a guess: '))

#     guesses_made += 1

#     if guess < number:
#         print ('Your guess is too low.')

#     if guess > number:
#         print ('Your guess is too high.')

#     if guess == number:
#         break

# if guess == number:
#     print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
# else:
#     print ('Nope. The number I was thinking of was {0}'.format(number))

# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'

# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)

# import random
# guesses_made = 0
# name = input("Hello! What is your name?\n ")
# print('Well, {0} I am thinking of a number between 1 and 20.'.format(name))
# number = random.randint(1,20)
# while guesses_made < 6:
#     guess = int(input('Take a guess: '))
#     guesses_made += 1
#     if guess < number:
#         print('Your guess is to low.')
#     if guess > number:
#         print('Your guess is to high.')
#     if guess == number:
#         break
#     if guess == number:
#         print('Good job, {0}, You guessed number in {1} guesses!'.format(name, guesses_made))
# else:
#     print ('Nope. The number I was thinking of was {0}'.format(number))


# list_users = ['admin','dev','design','manager','tester']
# # users = input('Enter your name: ')
# # profession = input('Enter your profession: ')
# for users in list_users:
#     if users == 'admin':
#         print(f"Hello {users}, would you like to see a status reports?")
#     else:
#         print(f"Hello {users}, thank you for logging in again.")
    
# current_users = ['admin','dev','design','manager','tester']
# new_users = ['admin','lamer','sam', 'ham', 'TESTER','dev']

# current_users_lower = [user.lower() for user in current_users]
# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print("Sorry " + new_user + ", that name is taken.")
#     else:
#         print("Great, " + new_user+ " is still available.")

# current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
# new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

# current_users_lower = [user.lower() for user in current_users]

# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print("Sorry " + new_user + ", that name is taken.")
#     else:
#         print("Great, " + new_user + " is still available.")

# usernames = []

# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print("Hello " + username + ", thank you for logging in again!")
# else:
#     print("We need to find some users!")


# numbers = list(range(1,11))
# for number in numbers:
#     if number == 1:
#         print("1st")
#     elif number == 2:
#         print("2nd")
#     elif number == 3:
#         print("3rd")        
#     else:
#         print(str(number) + "th")

# names = ['Inomjon','Numon','Uktam','Akbar']
# for name in names:
#     print(name+" is my best friend.")

# birth_year = int(input("Enter birth year: "))
# age = 2020 - birth_year
# print(age)

# weight_lbs = input("weight (lbs): ")
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)


# course = 'Python for beginners'
# print(course)
# print(course.replace('beginners','Absolute beginners'))

# i = 1
# while i <= 5:
#     print('*'*i)
#     i = i + 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you are failed!")


 
command = ""
started = False
while True:
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("Car already started!")
        else:
           started = True
           print("Car started...")
    elif command.lower() == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I dont understand you.")


