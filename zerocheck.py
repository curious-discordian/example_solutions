# Zero Check: 
# Write a function that checks a list of three integers and 
# returns true if any of them are zeros 

def zerocheck(ints):
    #this is the clearest way
    if 0 in ints:
        return True
    else: 
        return False

def zero_alt(ints): 
    # This is a silly one-liner way, but valid because integers are also "True", while 
    # 0 is "False", so 'not 0' = True, while 'not 1' = False. 
    # any([list of booleans]) will give true if any of the booleans are true 
    # otherwise it will return false
    return any([not i for i in ints])


integers = [0,10,3]
print(f'first the "normal" way:\n{zerocheck(integers)}')
print(f'and the alternative way:\n{zero_alt(integers)}')

"""
Run Sample 
$ python3 zerocheck.py 
first the "normal" way:
True
and the alternative way:
True

"""