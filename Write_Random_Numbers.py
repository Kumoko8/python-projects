#Taylor Golden
#Status: Complete

import random

def main():
    file_name = 'random_num.txt'
    amount = get_range()
    minimum = get_min()
    maximum = get_max(minimum)
    write_file(file_name, amount, minimum, maximum)

    print(f'File {file_name} written')
    

def get_range():
    
    num_range= int(input("How many random numbers would you like to generate?(1-100)"))

    while num_range < 1 or num_range > 100:
        print("Error: Number must be from 1 - 100")
        num_range= int(input("How many random numbers would you like to generate?(1-100)"))
    return num_range
    
def get_min():
    min_val= int(input("Choose minimum random number value (0-499)"))

    while min_val > 499 or min_val < 0:
        print("Error: Value must be from 0 - 499")
        min_val= int(input("Choose minimum random number value (0-499)"))
    return min_val
    
def get_max(x):
    max_val= int(input("Choose maximum random number value (1-500)"))

    while max_val > 500 or max_val < 1:
        print("Error: Value must be from 1 - 500")
        max_val= int(input("Choose maximum random number value (1-500)"))
    
    while x > max_val:
        print("Error: Value must be greater than the minimum one and less than 500")
        max_val= int(input("Choose maximum random number value (1-500)"))
    return max_val


def write_file(a, b, c, d):
    with open(a, 'w') as random_num_file:
         for n in range(b):
            random_num = random.randint(c, d)
            random_num_file.write(f'{random_num}\n')

      
if __name__=='__main__':
    
    main()
