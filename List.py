#Taylor Golden
#Status: Complete

user_list = []
while True:
    try:
        el_num = round(float(input('Enter number of elements in the list')))
        if el_num >=1:
            break
        else:
            print("The number must be 1 or more.")
    
    except ValueError:
        print("Incorrect data type.")
    except:
        print('An error has occurred.')
count = 0  
while count < el_num:
    try: 
        get_num = float(input('Enter a number'))
        if get_num >=1:
            user_list.append(get_num)
            count+=1
        else:
            print("The number must be 1 or more.")
    except ValueError:
        print('Incorrect data type.')
    except:
        print('An error has occurred.')
        
is_less = float(input('Enter a number you wish to test if the list items are greater than'))
found = False
greater_list = []
for item in user_list:
    if is_less < item :
        greater_list.insert(item)
        print(f'These numbers are greater than {is_less}: {item}')
        found = True

if not found:
    print(f'There are no numbers greater than{is_less}')
        
        
        # Create list with el_num elements
        
        
        
