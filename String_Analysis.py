#Taylor Golden
#STATUS: Complete

def main():
    try:
        with open('text.txt', 'r') as file:
            string = file.read()
        string_analysis(string)
    except FileNotFoundError:
        print("Error: 'text.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
   
        
def string_analysis(x):
    upper_count = 0
    lower_count = 0
    space_count = 0
    digit_count = 0
    
    for char in x:
        if char.isupper():
            upper_count+= 1
        elif char.islower():
            lower_count+= 1
        elif char.isdigit():
            digit_count+= 1
        elif char.isspace():
            space_count+= 1
    print(f'Uppercase letters: {upper_count}')
    print(f'Lowercase letters: {lower_count}')
    print(f'Whitespace Characters: {space_count}')
    print(f'Digits: {digit_count}')
    

if __name__=='__main__':
    
    main()
