#Lists

a = [1,2,3]
a.append('hi')

a.pop(a[0]) #takes off the end, starts at n - 1
print(a)
print(a[-1])#count from back
print(a[0:3])#print first 3
print(a[::2])#every two elements

letters = ['a', 'b', 'c']

matrix = [[0,1], [2,3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(20))
chars = list('Hello World')
print(len(chars))

a.insert(0, '_')#tell position and value
a.remove()
a.clear()


#unpacking
b =[1, 2, 3, 4, 4, 4, 4]
first, second, third = a

one, two, *other = b
print(other)


#Tuple is read only list
student = ('bro', 21, 'male')

for x in student:
    print(x)
if "bro" in student:
    print('yes')
    
#Loop through list
for item in a:
    print(item)
    
for index, item in enumerate(a):
    print(index, item)
    #prints index and item
    
print(a.count('d'))
    