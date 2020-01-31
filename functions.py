# def greet_user_kwd(name, lastname = ''):
#     """Functions to greet the user with name"""
#     return(f'hello, {name} {lastname}!')

# # calling the functions
# print(greet_user_kwd('John'))


# def triangle_area(height=0, base=0):
#     return height * base * 0.5

# print(triangle_area(4, 5))


def describe_city(city, country='Uzbekistan'):
    """return the message with city and country"""
    return (f'{city.title()} is in {country.title()}')

print(describe_city('\nTashkent'))
print(describe_city('\nparis', 'france'))
print(describe_city('\ndushanbe', 'tajikistan\n'))

def remove_duplicte(analyst):
    return set(analyst)
print(remove_duplicte([2,3,4,5,6,78,98,5,4,21,54,54,5,45,2,2,3,54,7,8,78,574,54,654,67,8797,65,64]))
