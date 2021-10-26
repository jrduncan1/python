# 1. Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]]
x = [ [5,2,3], [10,8,9] ]
def update_x(some_list):
    some_list[1][0] = 15

update_x(x)
print(x)

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def update_name(some_list):
    some_list[0]['last_name'] = 'Bryant'

update_name(students)
print(students)

# 3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def update_sports_dir(some_dict):
    some_dict['soccer'][0] = 'Andres'

update_sports_dir(sports_directory)
print(sports_directory)

# 4. Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

def update_z(some_list):
    some_list[0]['y'] = 30

update_z(z)
print(z)

###############################

# 2. Create a function iteratesome_dictionary(some_list) that, given a list of some_dictionaries
# the function loops through each some_dictionary in the list and prints each key and the 
# associated value.

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iteratesome_dictionary(student_list):
    for student_dict in student_list:
        f_name = student_dict['first_name']
        l_name = student_dict['last_name']
        print(f"first_name: {f_name}, last_name: {l_name}")

iteratesome_dictionary(students)

# # 2 BONUS
# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iteratesome_dictionary(list):
#     for idx in range(len(students)):
#         print(f"{'first_name'} {'last_name'}")
#     return(students)

# iteratesome_dictionary(students)

# 3. Get Values From a List of some_dictionaries
# Create a function iteratesome_dictionary2(key_name, some_list) that, given a  list of some_dictionaries and a key name, 
# the function prints the value stored in that key for each some_dictionary. For example, iteratesome_dictionary2('first_name', students) should output:

def iteratesome_dictionary2(key_name,some_list):
    for idx in range(len(students)):
        print(students[idx][key_name])
    return students

iteratesome_dictionary2('first_name',students)
iteratesome_dictionary2('last_name',students)


# 4. Iterate Through a some_dictionary with List Values
# Create a function printInfo(some_some_dict) that given a some_dictionary whose values are all lists, prints the name of each key along 
# with the size of its list, and then prints the associated values within each key's list.
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dictionary):
    for key in dictionary:
        length_of_list = len(dictionary[key])
        print(f'{length_of_list} {key.upper()}')
        for name in dictionary[key]:
            print(name)
        print()
print_info(dojo)