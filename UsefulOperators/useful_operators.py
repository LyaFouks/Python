# for x in range(3, 11, 4):
#     print(x)
# print(list(range(5)))

# letter_index = 0
# my_string = 'gsdgweqa'
# for letter in my_string:
#     print(letter + ' is at index ' + str(letter_index))
#     letter_index = letter_index + 1

# my_string = 'gsdgweqa'
# for index, letter in enumerate(my_string):
#     print(letter + ' is at index ' + str(index))

# print('a' in 'Jack')
# print('g' in 'Jack')
# print(str(2) in 'Jack')
# print('11' in 'Jack')
#
# letter_list = [a, b, c, d, True]
# print('a' in letter_list)
# print(True in letter_list)

# dict_1 = {1: 'a', 2: 'b', 3: 'c'}
# print(1 in dict_1)
# print(2 in dict_1.keys())
# print(4 in dict_1.keys())
# print('c' in dict_1.values())
# print('z' in dict_1.values())

# print(min(1, 3, 4, 51, 12))
# print(max(1, 3, 4, 51, 12))
#
# my_list = [1, 3, 4, 51, 12]
# print(min(my_list))
# print(max('Hello'))
#
# for letter in "Hello":
#     print(ord(letter))

from random import shuffle
my_list = [1, 3, 4, 51, 12]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(12, 20))
