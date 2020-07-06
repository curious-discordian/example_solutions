# Days in month. 
# The conditionals are easy here, but the input may vary. 
# We'll need to deal with lower vs uppercase here, but to ensure 
# the correct formatting on the names of the months we can use .capitalize()
# this means that cases like 'january', 'JANUARY', and 'JaNuArY' are all 
# interpreted as 'January'. (makes it more graceful wrt other ways of entering the input.)

month = input('Enter month:\n> ').capitalize()

if month in ['January' ,'March' ,'May' ,'July' ,'August' ,'October' ,'December']:
    print('31 days')
elif month in ['April', 'June' ,'September' ,'November']:
    print('30 days')
elif month == 'February':
    year = int(input('Enter year: \n> '))
    if ((year % 4 == 0) and not(year % 100 == 0)) or ((year % 4 == 0) and (year % 400 == 0)):       
        print('29 days')    
    else: 
        print('28 days')  
else: 
    #slight change here; we need to tell the user why their input was wrong.
    # and not just that it was wrong
    print('invalid input.\nplease input the month by name.')
    
"""
Run Samples: 
$ python3 daysinmonth.py 
Enter month:
> january
31 days

$ python3 daysinmonth.py 
Enter month:
> fEbRuary
Enter year: 
> 2020
29 days

"""