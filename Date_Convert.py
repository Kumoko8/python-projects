#Taylor Golden 
#STATUS: Complete
months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)
month_string = ' '.join(months)
month_list = month_string.split()
#Now Jan is month_list[0]
print(month_list[0])
def main():
    #takes user input date and calls isdate function
        user_date = input('Please enter a date in the format mm/dd/yyyy')
        
        date_result = isdate(user_date)
        
        if date_result:
            print('hi')
            
   
        
#def isdate():
    #accepts the input string and validates it
#    while True: 
#    try:
#         except ValueError:
#        print('Invalid Data')
#    except 
        