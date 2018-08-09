my_stuff = {'apple': "I AM APPLES!"}
print(my_stuff['apple'])

import mystuff

mystuff.apple()
print(mystuff.tangerine)

my_stuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable

# classess 
print('~~~' * 20)
class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between."

	def apple(self):
		print("I AM CLASSY APPLES!")


# instantiate = create; like import for modules
# instantiate a class => what you get is called an object
print('~~~' * 10)
print(MyStuff.apple(self))
print(MyStuff.tangerine)
print('~~~' * 5)
thing = MyStuff() # this is the instantiate operation, like calling a function
thing.apple()
print(thing.tangerine)
