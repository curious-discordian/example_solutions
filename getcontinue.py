# Get Continue
# write a function that continually prompts the user until a valid input 
# is entered .
# again using a trick with string formatting here, this time .lower() to 
# cast any strings to lowercase
# also using recursion to avoid the while-loop. 

def getContinue():
    choice = input('Do you want to continue (y/n)?\n> ').lower()
    if choice in ['y','n']: 
        return choice
    else: 
        print('please enter a valid choice...')
        return getContinue()
    
# Might also be a good idea to print the function-call so we can verify 
# that it returned what it should.
print(getContinue())

"""
Run Sample: 
$ python3 getcontinue.py 
Do you want to continue (y/n)?
> no
please enter a valid choice...
Do you want to continue (y/n)?
> n
n
"""