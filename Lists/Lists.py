# number_list = [32, 43, 51, 5.35, 223]
# print(number_list)
# some_list = [12, 414.12, "hello"]
# print(some_list)
# print(len(some_list))
# print(some_list[1])
# another_list = some_list[:2]
# print(another_list)
# some_list[2] = 'hi'
# print(some_list)
# new_list = some_list + another_list
# print(new_list)
#
# # Adding items
#
# # new_list[5] = 'new item'
# new_list.append('new item')
# new_list.insert(0, 'start')
# new_list.insert(2, 13)
#
# #Removing items
#
# # new_list.pop()
# # new_list.pop(0)
# # new_list.pop(-3)
#
# deleted_item = new_list.pop()
# deleted_item = new_list.pop(-3)
#
# deleted_item = new_list.remove(12)
#
# print(new_list)
# print(deleted_item)

number_list = [12, 34.5, 131, -1241, 123]
letter_list = ['s', 'w', 't', 'q']

x = number_list.sort()
letter_list.sort()
new_list = letter_list
print(number_list)
print(letter_list)
print(x)
print(new_list)

number_list.reverse()
letter_list.reverse()

number_list.append(letter_list)

print(number_list)
print(letter_list)
