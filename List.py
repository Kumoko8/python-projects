#Taylor Golden
#Status: Complete
def main():
    user_size = getListSize()
    user_items = getListItems(user_size)
    testList(user_items)
    

def getListSize():
    while True:
        try:
            el_num = round(float(input('Enter number of elements in the list ')))
            if el_num >=1:
                break
            else:
                print("The number must be 1 or more.")
    
        except ValueError:
            print("Incorrect data type.")
        except:
            print('An error has occurred.')
    return el_num

def getListItems(el_num):
    count = 0  
    user_list = []
    while count < el_num:
        try: 
            get_num = float(input('Enter a number '))
            if get_num >=1:
                user_list.append(get_num)
                count+=1
            else:
                print("The number must be 1 or more.")
        except ValueError:
            print('Incorrect data type.')
        except:
            print('An error has occurred.')
    return user_list
def testList(user_list):    
    is_less = float(input('Enter a number you wish to test if the list items are greater than '))
    found = False
    greater_list = []
    for item in user_list:
        if is_less < item :
            greater_list.append(item)
            found = True
    if found:
        print(f'These numbers are greater than {is_less}: {greater_list}')  
    else:
        print(f'There are no numbers in your list greater than {is_less}')
        
if __name__=='__main__':
    
    main()
        
        
        
