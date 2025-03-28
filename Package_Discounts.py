#Taylor Golden
#Status: Complete
UNIT_PRICE = 149.0

num_packages = float(input("Enter the number of packages purchased"))
while num_packages <=0:
        print('Error: Incorrect number of packages')
        num_packages = float(input("Enter the number of packages purchased"))
subtotal = num_packages * UNIT_PRICE 
if num_packages >= 150:
        discount = subtotal * 0.4
elif num_packages >=100:
        discount = subtotal * 0.3
elif num_packages >=50:
        discount = subtotal * 0.2
elif num_packages >=10:
        discount = subtotal *0.1
else:
    discount = 0
              
total = subtotal - discount

print(f'Discount amount: {discount}\n Total after discount: {total}')