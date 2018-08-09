# def my_function(*args):
# 	arg1, arg2, arg3 = args
# 	print(f"I'm trying to figure out what this function should do")
# 	print(f"I'm testing if arg1 + arg2 equals {arg1 + arg2} ")
# 	print(f"{arg3} is just for fun")

# my_function(1, 2, 3)

# item1 = "banana"
# item2 = "nana"
# item3 = "banananananana"

# my_function(item1, item2, item3)

# l = 'abcdefg'
# l['a']

# symbols = 'abcdefghijklmnopqrstuvwxyz '
# # message = 'aaabbc'
# key = 1
# coded_message = ''

# for char in message:
# 	if char in symbols:
# 		index_char = symbols.find(char)
# 		coded_index = index_char + key
# 		coded_message += symbols[coded_index]
# print(coded_message)

# message = 'bbbccd'
# decoded = ''


# for char in message:
# 	if char in symbols:
# 		message_index = symbols.find(char)
# 		decoded_index = message_index - key
# 		decoded += symbols[decoded_index]

# print(decoded)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
print("Tell me your secret message, you wildling: ")
message = input()
print("Now tell me what key you wish to use to code your message (must be a number): ")
key = int(input())
coded_message = ''
decoded_message = ''
# print(len(SYMBOLS))


for char in message:
	if char in SYMBOLS:
		char_index = SYMBOLS.find(char)
		coded_index = (char_index + key) % 66
		coded_message += SYMBOLS[coded_index]

	else:
		coded_message += char		

print(f"Your coded text is: {coded_message}")


for char in message:
	if char in SYMBOLS:
		char_index = SYMBOLS.find(char)
		decoded_index = (char_index - key) % 66
		decoded_message += SYMBOLS[decoded_index]
	else:
		decoded_message += char

print(f"Your decoded message is: {decoded_message}")















