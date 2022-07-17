greeting = "Hello"
first_name = "Jack"
last_name = 'White'
exclamation_sign = "!"
white_space = " "
whole_sentence = greeting + white_space + first_name + white_space \
                 + last_name + exclamation_sign
print(whole_sentence)
long_string = "This is the long string"
print(long_string)

#Escaping \
some_string = 'I\'m a programmer'
print(some_string)
another_string = "I want to learn \"Python\""
print(another_string)

string_with_new_lines = "Hello! \n   \rMy name is Nikita"
print(string_with_new_lines)

numbers = "1\t2345\t67"
print(numbers)
some_text = "\tHello! \n\tI'm very glad to see you!"
print(some_text)

#Triple quotes
string_with_triple_quotes = """This is '
text with 
"triple 
quotes" """
another_string_with_triple_quotes = '''This is ' text with "triple quotes" '''
print(string_with_triple_quotes)
print(another_string_with_triple_quotes)