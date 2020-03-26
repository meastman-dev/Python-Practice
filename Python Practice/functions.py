def greet_user(username):
    print(f"Hello, {username}")
greet_user('mason')

def display_message(message):
    print(message)
display_message(f"Today I will be learning about Python functions")

def favorite_book(book_title):
    print(f"One of my favorite books is {book_title}")
favorite_book("Alice in Wonderland")

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
#order doesnt matter with keyword arguments

def make_shirt(shirt_size, shirt_message):
    print(f"\nShirt Size: {shirt_size}")
    print(f"Shirt Message: {shirt_message}")
make_shirt('XL', 'Hello boy')
make_shirt(shirt_size='XL', shirt_message='Hello boy')

#default arguments
def make_shirt(shirt_size='L', shirt_message='I love Python'):
    print(f"\nShirt Size: {shirt_size}")
    print(f"Shirt Message: {shirt_message}")
make_shirt()
make_shirt('M')
make_shirt('S', 'Just kidding, I love JavaScript')
print()

#return functions
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print()

def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name2('jimi', 'hendrix')
print(musician)
musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)

#returning dictionaries
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def get_formatted_name3(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("Press Q at any time to quit")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name3(f_name, l_name)
    print(f"Hello, {formatted_name}!")

def print_models(unprinted_designs, complete_models):
    #accepts unprinted_designs lists, and empty complete_models list
    while unprinted_designs:
        current_design = unprinted_designs.pop() #while unprinted_designs is occupied, pop the list
        print(f"Printing model: {current_design}") #print each item being popped from lists
        complete_models.append(current_design) #store each popped item into a new list called complete_models

def show_completed_models(complete_models):
    print("\nThe following models have been printed:")
    for complete_model in complete_models:
        print(complete_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []
print_models(unprinted_designs, complete_models)
show_completed_models(complete_models)

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


