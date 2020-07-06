# Oil in the Bank Check: 
# Note; description here is a little unclear, as to whether it should 
# request input from the user, but let's assume that's made clear 
# 
# Also it may be good to state that it should be a function

def oilcheck(current): 
    # takes an int as input, 
    if current in range(7000,7500):
        print('early warning')
        print(f'remaining miles: {7500 - current}')
    elif current >= 7500:
        print('Warning Triggered, over 7500 since last oilcheck.')
    else: 
        print(f'all good, remaining {7500 - current}')
        
user_input = int(input('please input your mileage <int>:\n> '))
oilcheck(user_input)

"""
Run sample: 
$ python3 oilcheck.py 
please input your mileage <int>:
> 7500
warning

$ python3 oilcheck.py 
please input your mileage <int>:
> 7005
early warning
remaining miles: 495

"""