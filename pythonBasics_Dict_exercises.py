# 01/19/2020

# Sortling the lists

# nums=[23,6,890,1,0,-3,-9]
# print(nums)
# nums.sort()
# print(nums)
# nums.append(45)
# print(nums)
# nums.sort()
# print(nums)


#Sorting the list temporarily

# words = ['hello','world','of', 'engineers', 'hightech', 'python','!']
# sorted_words = sorted(words)
# print(sorted_words)
# print(words)


# nums=[-8,2,65,84,12,0,9,8,5,4,6,2,1,45]
# nums.reverse()
# print(nums)
# nums.sort()
# print(nums)

# word = list('Hello')
# word.reverse()
# print(word)
# print(''.join(word))
# print(*word)

# find the polindrome
# get the input from the user(one only)
# return to the user this word polindrome or not
# word = list(input("Please enter your word: "))
# reverse_word = word.reverse()
# if word == word.reverse():
#     print(f"This {word} is polindrome!")
# else:
#     print(f"This {word} is not polindrome")


# word = list(input("Please enter your word: "))
# reverse(word)
# print(word.reverse())

# s = input('Please type in your full name')   reverse last name 
# print(' '.join(reversed(s.split(' '))))


# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
    
#     if word == (word[char]):
#       print(f"This {word} is a polindrome!")
#     else:
#         print(f"This {word} is not a polindrome!")


# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
#     print(word[char], end="")

# word = input("Please enter your word: ")
# if word == (list(reversed(word))):
#     print(f"This {list} is a polindrome!")





    # if char == print:
    #     print(f"This {print} is a polindrome!")
    # else:
    #     print(f"This {print} is not a polindrome!")


# word = input("Please enter your word: ")
# if word == (word[::-1]):
#     print(f"\n{word} is a palindrome!\n")                 # comparing with palindrome words
# else:
#     print(f"\n{word} is not a palindrome!\n")


# word = input("Please enter your word: ")

# lword = list(word)
# lword.reverse()

# if ''.join(lword) == word:                              # comparing with palindrome words
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not palindrome, dont you see!")


# name = input('Please type in your full name')
# name = name.split()
# print (name[-1] + ',', ' '.join(name[:-1]))


# split - the opposite of ''.join() function, split will return you the list

# msg = 'Hello everyone, we are doing some exercises on python'
# words = msg.split(',')
# print(words) # when splitted by space

# msg = 'price is $100.00'
# # print the new price if 20% discount is applied
# price = msg.split('$')[1]
# int_price = float(price)
# dis_price = int_price * 0.8
# print(f"discounted price is {dis_price}")

# print(f"discounted price is {float(msg.split('$')[1])*0.8}")

# Print the capitals of the countries
# create repository for 10 countries with their capital cities
# when user enters the country print the capital city
# return >> "Capital city of UK is London."
# countries = {'Afghanistan': 'Kabul', 'Albania':'Tirana','Algeria':'Algiers','Andorra':'Andorra la Vella', 'Angola': 'Luanda'}
# msg = input('enter the country: ')
# isExist = False #Flagging

# # if msg.upper() in countries.keys:
# for key in countries.keys():
#     if msg.upper() == key.upper():
#         isExist = True
# if isExist:
#     print(f"Capital city of {msg.title()} is {countries[msg].title()}.")
# else:
#     print(f"{msg} does not exist in our database.")

# while loops

# num = 5
# while num < 10:
#     print('I am awake! opening my eyes...')
#     num +=1


# msg = ''
# while   msg.lower() != 'quit':
#     msg = input('I am a Tom, tell me the word I will repeat it loudly: ')  # repeating inputs over and over again
#     print(msg.upper())

# msg = ''
# stop_signal = True
# while  stop_signal:
#     msg = input('I am a Tom, tell me the word I will repeat it loudly: ')  # repeating inputs over and over again
#     print(msg.upper())
#     if msg.lower() == 'quit': #Flagging
#         stop_signal = False


# BREAK, continue

# while True:
#     msg = input('I am a Tom, tell me the word I will repeat it loudly: ')  # repeating inputs over and over again
#     print(msg.upper())
#     if msg.lower() == 'quit': #Flagging
#         break

# find given number from the list and print the message if exists.
# nums = [12,34,5,0,45,21,54,87,4,6,65,45,87,787,2,121,54,4,87,99,8,656,55,45,4]
# key_num = int(input('enter the number: '))
# for num in nums:
#     if key_num == num:
#         print(f"{key_num} is found, stopping the search...")          # search number is found stops
#         break
#     else:
#         print(f"{key_num} was not found, searching...")


# nums = [12,34,5,0,45,21,54,87,4,6,65,45,87,787,2,121,54,4,87,99,8,656,55,45,4]
# key_num = int(input('enter the number: '))
# for num in nums:
#     if key_num == num:
#         print(f"{key_num} is found, stopping the search...")
#         continue
#     else:
#         print(f"{key_num} was not found, searching...")



