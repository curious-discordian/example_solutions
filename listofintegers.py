
input_from_user = input('please give a list of integers separated by space:\n> ').split()
# use split to separate (default is separating on whitespace)
list_of_integers = [int(integer.strip()) for integer in input_from_user]
# the strip-method will clear any surrounding whitespace, and is 
# not strictly necessary here, since we're using whitespace as the 
# separation-character.
# Also the surrounding square-brackets with the loop syntax is known as 
# list-comprehension. 
print('Of the provided integers, these were between 1-100')
# using both list comprehension and string formatting: 
print(f'{[i for i in list_of_integers if i < 100 and i > 1]}')
    
"""
Run sample: 
$ python3 listofintegers.py 
please give a list of integers separated by space
> 0 23 100 99 101 1 4
Of the provided integers, these were between 1-100
[23, 99, 4]
"""

# Further notes, once the list of input is made, it's possible to also 
# use the builtin filter(func, list) by creating the function to give as 
# def criteria(x): 
#     if x < 100 and x > 1: 
#         return True
#     else: 
#         return False
#
# filter however returns a filter-object, so we'll have to tell it to 
# become a list by doing list(filter(criteria, our_list))
 
