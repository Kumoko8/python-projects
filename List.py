#Taylor Golden
#Status: Complete
def main():
    #controller function 
    user_size = getListSize()
    user_items = getListItems(user_size)
    n = get_test_num()
    display_larger(user_items, n)
    
def getListSize():
    #gets size of list from user and validates
    while True:
        try:
            if (el_num := round(float(input('Enter number of elements in the list '))))>=1:
                break
            else:
                print("The number must be 1 or more.")
    
        except ValueError:
            print("Incorrect data type.")
        except:
            print('An error has occurred.')
    return el_num

def getListItems(el_num):
    #gets the items from user, validates and puts them in array
    count = 0  
    user_list = []
    while count < el_num:
        try: 
            if(get_num := float(input('Enter a number '))) >=1:
                user_list.append(get_num)
                count+=1
            else:
                print("The number must be 1 or more.")
        except ValueError:
            print('Incorrect data type.')
        except:
            print('An error has occurred.')
    return user_list
def get_test_num():
    while True:
        try: 
            n = float(input('Enter a number you wish to test if the list items are greater than '))
            return n
        except ValueError:
            print('Incorrect data type.')
        except:
            print('Error occurred.')
    
    
def display_larger(user_list, n): 
    #gets a number to test and gives array that passes test or not   
    
    found = False
    greater_list = []
    for item in user_list:
        if n < item :
            greater_list.append(item)
            found = True
    if found:
        print(f'These numbers are greater than {n}: {greater_list}')  
    else:
        print(f'There are no numbers in your list greater than {n}')
        
if __name__=='__main__':
    
    main()
        
        
        
