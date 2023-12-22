# Defining a Function
def greet_user():
    '''Display a simple greeting.'''
    print("Hello!")

greet_user()

# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!") #.title() is a string method in Python that capitalizes the first letter of each word in a string. For example, "hello world".title() would return "Hello World".
# An f-string, or formatted string literal, is a feature introduced in Python 3.6 that provides a concise and convenient way to embed expressions inside string literals. It allows you to directly embed expressions and variables inside the string, instead of concatenating them with the + operator.
# An f-string is created by prefixing a string literal with the letter "f" (or "F"), and then enclosing expressions in curly braces {} within the string. The expressions inside the curly braces are evaluated at runtime, and their values are formatted into the string.
greet_user('jesse')

# Practice1
def display_message():
    print("Function")

display_message()

def favorite_book(title):
    print(f"My favorite book is {title}.")

favorite_book('Alice in Wonderland')

# Passing Arguments
# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.") # \n is a special character sequence called a newline character. It is used to represent the end of a line and creates a new line for the subsequent text to be printed. In this code, it creates a blank line before the sentence "I have a {animal_type}." is printed.
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Multiple Function Calls
describe_pet('dog', 'willie')

# Order Matters in Positional Arguments
describe_pet('harry', 'hamster')

# Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet('harry', 'hamster')

# Avoiding Argument Errors
# describe_pet()

# Practice2
def make_shirt(size, text):
    print(f"\nThe shirt is of size {size.title()}.")
    print(f"It prints a word {text}.")

make_shirt('l', 'python')
make_shirt(size='m', text='r')

def make_shirt(size='L', text='I love Python'):
    print(f"\nThe shirt is of size {size.title()}.")
    print(f"It prints a word {text}.")

make_shirt()
make_shirt('m')
make_shirt(text='haha', size='s')

def describe_city(city_name, country_name='China'):
    print(f"\n{city_name.title()} is in {country_name.title()}.")

describe_city('beijing')
describe_city('shanghai')
describe_city('new york')

# Return Values
# Returning a Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age = None):
    person = {'first': first_name, 'last': last_name}
    if age:
     person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {last_name}"
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)

# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ") #In programming, input() is a built-in function in many programming languages, including Python, that allows you to accept user input during program execution.

    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def city_country(city_name, country_name):
    full_name = f"{city_name}, {country_name}"
    return full_name.title()

while True:
    c_name = input("City Name: ")
    if c_name == 'q':
        break

    C_name = input("Country Name: ")
    if C_name == 'q':
        break

    ccname = city_country(c_name, C_name)
    print(ccname)

# practice
def make_album(artist_name, album_title):
    full_name=f"{artist_name}, {album_title}"
    return full_name.title()

while True:
    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("album title: ")
    if a_title == 'q':
        break

    m_album = make_album(a_name, a_title)
    print(m_album)

# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# modifying a List in a Function
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop() #In programming, pop() is a method or function that removes and returns the last element from a list or array.
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robor pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# preventing a Function from Modifying a List
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

# Practice
def show_message(messages):
    for message in messages:
        text = f"{message}"
        print(text)

msg = ['hello', 'Kk', 'bye']
show_message(msg)

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        sending_messages=unsent_messages.pop()
        print(f"{sending_messages} is sending.")
        sent_messages.append(sending_messages)

unsent_message = ['hello', 'Kk', 'bye']
sent_message = []

send_messages(unsent_message[:], sent_message)
print(unsent_message)

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# practice
def make_sandwiches(*ingredients):
    print("The sandwich has the following ingredients:")
    for ingredient in ingredients:
        print(f'-{ingredient}')

make_sandwiches('beef', 'chicken', 'tomato')
make_sandwiches('cheese', 'ham')
make_sandwiches('tuna', 'egg')

def build_profile(first, last, **user_info):
    user_info['first_nmae'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Di', 'Kang', location='newark', field='economics', age='28')
print(user_profile)

def make_cars(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_cars('honda', 'civic', milages = '1000', color = 'black', sedan = True)
print(car)

# Storing Your Functions in Modules
# Importing an Entire Module

