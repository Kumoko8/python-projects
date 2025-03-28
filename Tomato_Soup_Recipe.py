#Taylor Golden
#Status: Complete

dish_name= "tomato soup"

ingredients = [2.0, 0.333, 2.0, 1.0]
num_servings = float(input('Enter the number of servings you want to make '))

serving_amt = [x * num_servings for x in ingredients]

print(f"To make {num_servings} servings of {dish_name} you will need:\n {serving_amt[0]:.2f} cups of tomato sauce\n{serving_amt[1]:.2f} cups of tomato paste\n {serving_amt[2]:.2f} cloves of garlic and \n {serving_amt[3]:.2f} tablespoons of oregano ")

