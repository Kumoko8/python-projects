#Taylor Golden
#Status: Complete

user_list = []
while True:
    try:
        el_num = round(float(input('Enter number of elements in the list')))
        if el_num > 1:
            break
        else:
            print("The number must be 1 or more.")
    
    except ValueError:
        print("Incorrect data type.")
count = 0  
while count < 5:
    try: 
        get_num = float(input('Enter a number'))
        if get_num > 1:
            user_list.append(get_num)
            count+=1
        else:
            print("The number must be 1 or more.")
    except ValueError:
        print('Incorrect data type.')
    
        
        # Create list with el_num elements
        
        
        
