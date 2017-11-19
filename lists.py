# an empty list
empty = []
print(empty)

# list of string
str = ['Dave', 'Angela', 'Chloe', 'Charlotte']
print(str)

# list of number
nums = [36, 34, 6, 3]
print(nums)

# list of mixed item
mixed = ['Dave', 20, 'hello', 1.765]
print(mixed)

# indices and slicing
greetings = ['aloh', 'hello', 'hola']
print(greetings[0])
print(greetings[0:2])
print(greetings[1:])
print(greetings[1:])

# adding
brit_slang = ['cheerio', 'pip', 'smashing']
brit_slang.append('brilliant')
print(brit_slang)

# removing
brit_slang.remove('pip');
print brit_slang

del brit_slang[0]
print brit_slang

words = ['the', 'at', 'girl', 'song', 'bird']
del words[:2]
print words