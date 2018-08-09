# empty dictionary
empty = {}
print(empty)

# create dictionary of dictionaries

en_de = { 
"red": "rot",
"green":  "grun",
"blue": "blau",
"yellow": "gelb"
}

de_fr = {
	"rot": "rouge",
	"grun": "vert",
	"blau": "bleu",
	"gelb": "jaune"
}

dictionaries = {
	"en_de": en_de,
	"de_fr": de_fr
}
print(dictionaries["de_fr"]["blau"])

print('<>' * 15)
"red" in en_de

# Operators and Dictionaries: 
# len(d) = returns the no. of stored entries, e.g. no of (key, value) pairs
# del d[k] = deletes the key k together with its value
# k in d = True if a key exists in dictionary d
# k not in d = Ture if a key doesn't exist in dict d

# copy a dictionary
words = {"house" : "Haus", "cat":"Katze"}
w = words.copy()
words["cat"] = "chat"
print(w)
print(words)

# clear a dict and NOT delete it
w.clear()
print(w)

# list(d) extracts all the keys in the dictionary in a list, in insertion order; if you wanted sorted 
# you use sorted(d) instead

print('<@>' * 20)
print(list(en_de))
print(sorted(en_de))

# loop with  the items() method
knights = {'galileo': 'the wise', 'magellan': 'the bold', 'eddison': 'the idea man'}
for key, value in knights.items():
	print(key, value)

# an ordered dictionary - .OrderedDict
import collections

print("Regular dicionary: ")
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
	print(k, v)

print("\nOrderedDict:")
d = collections.OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
	print(k, v)

import collections

print('dict       :',)
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

print('OrderedDict:',)

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)


# # get the position index and corresponding value when looping through a sequence with enumerate()
# for k, v in enumerate(['tic', 'tac', 'toe']):
# 	print(k, v)



# # loop over two or more sequences at the same time, the entries can be paired with zip:
# for k, v in zip(questions, answers):
# 	print("What is your {0}? It is {1}.".format(k, v))


# # loop over a sequence in reverse: first specify the sequence in a forward direction, and then call 
# # the reversed function
# for i in reversed(range(1, 10, 2)):
# 	print(i)

# # loop over a sequence in sorted order with sorted(); note: it returns a new sorted list, 
# # the previsou list stays the same

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
# 	print(f)






