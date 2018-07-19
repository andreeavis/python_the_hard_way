tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat= '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)



x = 22
y = 11
z = 'apples'
fruits = '\tIlove fruits. this is tabbed'
fruits_count = f'There are {x}\nfruits on the\n table.' 
fruits_and = f'''
\t* I love {z} so much.
\t* I also love mangos.
\t* I don't know what to write next.
\t* How many fruits are there on the table?
\t* There are {x + y} fruits.
'''

print(fruits)
print(fruits_count)
print(fruits_and)
