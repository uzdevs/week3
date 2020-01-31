# n = input('enter your number: ')
# fillchar = '#'
# for fill in fillchar:
#     print(n.rjust(fillchar))

# txt = 'Banana'
# x = txt.rjust(60)
# print(x, ' is my favorite fruit.')


# for i in range(10,1,-1):
#     print("{:<19}".format(" ".join(map(str,range(i)))))

# cstr = "I love geeksforgeeks"
  

# # Printing the center aligned  
# # string with fillchr 

# print (cstr.center(40, '#')) 

# n = "This is my simple code."
# for i in range(len(n)):
#     print(n.center(50, '#'))

# numbers = [11,33,55,39,55,75,44,37,21,23,41,13]

# for num in numbers:
#    if num%2 == 0:
#       print ('the list contains an even number')
#       break
# else:
#    print ('the list doesnot contain even number')

# string = " Hello World "
# for x in string:
#     print(x.center(40, '#'))


# Complete the staircase function below.
# n = input('Enter')
# for i in range(1, n + 1):
#        print(' '.join(n))
            

# n = int(input())
# s = '#'
# for i in range( 1 , n+1):
#     print (" "*(n-i) + s*i)

# n = int(input())
# for i in range(1, n + 1):
#         print(str('#'*i).center(n))

# for i in range(n):
#     s = "#" * (i + 1)
#     print(s.center(n, " "))


# n = int(input("Please enter your number: "))
# for i in range(n):
#     s = "#" * (i + 1)
#     print(s.rjust(n, " "))

    
# month = input("Please enter month: ")
# month_store = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October','November', 'December']
# if month in month_store:
#     print(month.center(40,'#'))
# for i in range(1,32):
#     print(i)


# month = input("Please enter month: ")
#  calendar = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October','November', 'December']
calender = [('January', range(1, 31 + 1)),
            ('Feburary', range(1, 28 + 1)),
            ('March', range(1, 31 + 1)),
            ('April', range(1, 30 + 1)),
            ('May', range(1, 31 + 1)),
            ('June', range(1, 30 + 1)),
            ('July', range(1, 31 + 1)),
            ('August', range(1, 31 + 1)),
            ('September', range(1, 30 + 1)),
            ('October', range(1, 31 + 1)),
            ('November', range(1, 30 + 1)),
            ('December', range(1, 31 + 1))]

def make_calendar(year, start_day):
    for month, days in calender:
        # Print month title
        print('{0} {1}'.format(month, year).center(20, ' '))
        # Print Day headings
        print(''.join(['{0:<3}'.format(w) for w in week]))
        # Add spacing for non-zero starting position
        print('{0:<3}'.format('')*start_pos, end='')

        for day in days:
            # Print day
            print('{0:<3}'.format(day), end='')
            start_pos += 1
            if start_pos == 7:
                # If start_pos == 7 (Sunday) start new line
                print()
                start_pos = 0 # Reset counter
        print('\n')
    
yr=int(input('Enter Year: '))
strtday=input('Enter start day of the year Mo,Tu,We,Th,Fr,Sa,Su: ')
make_calendar(yr,strtday)