# Taylor Golden
# STATUS: Complete

months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)
month_string = ' '.join(months)
month_list = month_string.split()
# Now Jan is month_list[0]
print(month_list[0])  # Just a test print

def main():
    # Takes user input and checks if it's a valid date
    while True:
        user_date = input('Please enter a date in the format mm/dd/yyyy: ')
        if isdate(user_date):
            split_date = user_date.split('/')
            month = int(split_date[0])
            day = int(split_date[1])
            year = split_date[2]
        
        # Get month name from month_list using index
            month_name = month_list[month - 1]
            print(f"The date is {month_name} {day}, {year}")
            break
        else:
            print("Invalid date.")

def isdate(x):
    if '/' not in x:
        return False

    input_list = x.split('/')
    if len(input_list) != 3:
        return False

    month, day, year = input_list

    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        return False

    month = int(month)
    day = int(day)

    if not (1 <= month <= 12 and 1 <= day <= 31):
        return False

    return True

if __name__ == '__main__':
    main()
