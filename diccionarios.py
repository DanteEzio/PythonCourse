# Data structure -> Lists, Dicts

# A dictionary is a data structure where we can have many data types grouped (as a list).
# The main difference between a dict and a list is that in a list we only have values,
# (i.e. [Martin, Arturo, Topi, Pablo, Chocho] or [1,2,3,4,5]).
# In dict we have a key-value pair values for each attribute into the dictionary.
# It means that now we have values into the dictionary, but each one of this values HAVE
# a key or identifier, a name which each attribute is identified.
# Also, the data into a dict is unordered.

user = {
    'age': 23,
    'first_name': 'Martin',
    'birth_date': '1997-03-21',
    'last_name': 'Melo Godinez',
}

# Properties
# - Dictionaries are defined using curly braces
# - Each attribute needs to have the following sintax key: value and needs to have a comma in the end of the line, to handle add more attributes. In the last line this comma is optional because we don't add more attributes.
# - Key are always string, so need to be quoted
# - Values can be of any type (int, string, boolean, none, float) even data structures (list, dictionaries)

# GET A KEY OF A DICT:
print(user['first_name'])

#What happens if the key doesn't exist
# print(user['gender']) # Throw an error :(

# How can we check if a key exist into a dict?
# print('first_name' in user)
# print('gender' in user)

if 'gender' in user:
    print(user['gender'])
else:
    print('Gender key does not exist')

if 'last_name' in user:
    print(user['last_name'])
else:
    print('Last Name key does not exist')

# Check if a key exist in the dict, and put default
print(user.get('country', 'México'))

# ADD NEW KEYS TO A DICT
user['email'] = 'martinmelo@actosoft.com.mx'
# print(user)

# UPDATE EXISTING KEYS IN A DICT
user['email'] = 'martin.melo.dev.97@gmail.com'
# print(user)

# DELETE KEYS IN A DICT
del user['email']
# print(user)

profile = {
    'profile_photo': 'pikachu.jpg',
    'RFC': 'AAA0101010AAA',
    'hobbies': 'Hacerme wey'
}

# Concatenate or join dicts
user.update(profile)
# print(user)

# Loop keys and values of a dict
for key, value in user.items():
    print("*********************")
    print("Key:", key)
    print("Value:", value) 