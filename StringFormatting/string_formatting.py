# # print(1 + 1)
# # print('1' + '1')
# # age = 23
# # print('Jake is '+ str(age) + ' years old.')
# # print('Jake is '+ str(23) + ' years old.')
#
#
# name = 'Jack'
# age = 23
# name_and_age = 'My name is {0}. I\'m {1} years old.'\
#     .format(name, age)
# print(name_and_age)
# name_and_age = 'My name is {0}. I\'m {1} years old.' \
#     .format('Jack', 23)
# print(name_and_age)
# name_and_age = 'My name is {}. I\'m {} years old.' \
#     .format(23, 'Jack')
# print(name_and_age)
#
# # week_days = 'There are seven days in a week: {2}, {0}, {1}, ' \
# #             '{3}, {4}, {5}, {6}'.format('Monday', 'Tuesday', 'Sunday', 'Wednesday',
# #             'Thursday', 'Friday', 'Saturday')
# # print(week_days)
#
# week_days = 'There are seven days in a week: {su}, {mo}, {tu}, ' \
#             '{we}, {th}, {fr}, {su}'.format(mo = 'Monday', tu = 'Tuesday', su = 'Sunday', we = 'Wednesday',
#                                         th = 'Thursday', fr = 'Friday', sa ='Saturday')
# print(week_days)


# float_result = 1000 / 7
# print(float_result)
# print('The result of division is {0:1.3f}'.format(float_result))
# print('''
# {0:10.2f}{1:10.2f}{2:10.2f}
# {3:10.2f}{4:10.2f}{5:10.2f}
# {6:10.2f}{7:10.2f}{8:10.2f}
# '''.format(1.5345345, 424.4513521, 123.41351, 31.5235,
#            1.5345345, 424.4513521, 123.41351, 31.5235,
#            1.5345345, 424.4513521, 123.41351, 31.5235))


name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'\
    .format(name, age)
print(name_and_age)
name_and_age = f'My name is {name}. I\'m {age} years old.'
print(name_and_age)

print('My name is %s. %s %d years old' % (name, "I'm", age))