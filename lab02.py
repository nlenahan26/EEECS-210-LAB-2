# Name: Nathan Lenahan
# KUID: 3178995 
# LAB Session (Day/Time): Wednesday 11am 
# LAB Assignment: Lab 02
# Description:
#
#
#
# Collaborators/Sources:

#   Note: if you are working in python, you are  
#   REQUIRED to call this function to get your
#   input, so all assignments are consistant 

#   Returns a list of number,letter pairs
def get_mapping_pairs() -> str:
    x = input("Enter your mapping pairs: ")
    items = x.replace("(","").replace(" ","").strip(")").split(")")
    pairs = []
    for item in items:
        pairs.append(item.split(","))
    return pairs

# Your Code Here

#Sample code
#With the following input: (3, A) (2, D) (3, C)
pair_list = get_mapping_pairs()

num_pairs = len(pair_list)
nums = ['0', '1', '2', '3',]
letters = ['A', 'B', 'C', 'D']



#Checks if a function
is_function = True
for x in nums:
    check = 0
    for pair in pair_list:
        if pair[0] == x:
            check += 1
    if check != 1:
        is_function = False

is_one_to_one = True
for x in letters:
    check = 0
    for pair in pair_list:
        if pair[1] == x:
            check += 1
    if check > 1:
        is_one_to_one = False



is_onto = False
inputted_letters =[]
for pair in pair_list:
    inputted_letters.append(pair[1])

if 'A' in inputted_letters and 'B' in inputted_letters and 'C' in inputted_letters and 'D' in inputted_letters:
    is_onto = True

result = ''

if is_function:
    result += 'function, '
else:
    result += 'not a function'

if is_function:
    if is_one_to_one:
        result += 'one-to-one, '
    else:
        result += 'not one-to-one, '

    if is_onto:
        result += 'onto'
    else:
        result += 'not onto'

print(result)