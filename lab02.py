# Name: Nathan Lenahan
# KUID: 3178995 
# LAB Session (Day/Time): Wednesday 11am 
# LAB Assignment: Lab 02
# Description: Determines if an input mapping is a function or not.
# If it is a function, it determines if it is one-to-one and onto.
# Collaborators/Sources: N/A

#Returns a list of number,letter pairs
def get_mapping_pairs() -> str:
    x = input("Enter your mapping pairs: ")
    items = x.replace("(","").replace(" ","").strip(")").split(")")
    pairs = []
    for item in items:
        pairs.append(item.split(","))
    return pairs

#Makes the pair list
pair_list = get_mapping_pairs()

#Stores the possible inputs and outputs and number of pairs
num_pairs = len(pair_list)
nums = ['0', '1', '2', '3',]
letters = ['A', 'B', 'C', 'D']


#Checks if every number has exactly one output (is a function)
is_function = True
for x in nums:
    check = 0
    for pair in pair_list:
        if pair[0] == x:
            check += 1
    if check != 1:
        is_function = False

#Checks if a letter is used as an output more than once (is one-to-one)
is_one_to_one = True
for x in letters:
    check = 0
    for pair in pair_list:
        if pair[1] == x:
            check += 1
    if check > 1:
        is_one_to_one = False

#The following two blocks check if the function is onto or not
#Creates a list of letters used as outputs
is_onto = False
inputted_letters =[]
for pair in pair_list:
    inputted_letters.append(pair[1])

#Checks to see if every letter is an output
if 'A' in inputted_letters and 'B' in inputted_letters and 'C' in inputted_letters and 'D' in inputted_letters:
    is_onto = True


#Makes the final result message based on the above checks
result = ''

if is_function:
    result += 'function, '
else:
    result += 'not function'

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