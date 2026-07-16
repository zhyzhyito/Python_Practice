#Which of the following is NOT a form of string concatenation?
#

#developer = 'Jessica'
#greeting = 'My name is ' + developer + '.'


#developer = 'Jessica'
#age = 30
#greeting = 'My name is ' + developer + ' and I am ' + str(age) + ' years old.'


#greeting = 'My name is '
#developer = 'Jessica'

#greeting += developer

#


#Which of the following functions is used to return the number of the characters in the string?
#Answer: len()


#What will result be in this example?

#developer = 'Naomi'

#result = developer.endswith('N')
#Answer: False


#What happens when you add a float and an integer?
#Answer: The result is a float.




#Which of the following is the correct way to define a function?

#def get_sum(num_1, num_2):
#    return num_1 + num_2


#def greet():
#    pass
    
#print(greet())


#Which of the following statements is false when naming variables?

#1.Variable names can only start with a letter or an underscore (_), not a number.
#2.Variable names can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
#ANSWER >> 3.Variable names must have a max length of 10 characters, otherwise Python will throw an error.
#4.Variable names cannot be one of Python's reserved keywords such as if, class, or def.




#What will be the result for the following code?
#message = 'Python is fun!'
#print(message[0:6])
#Answer: Python


#What does the split() method do?
#1.This method is used to split a float into a list of substrings.
#2.This method is used to split a dictionary into a list of substrings.
#3.This method is used to split a string into a list of substrings.
#4.This method is used to split a tuple into a list of substrings.



#example_list = ['example', 'dashed', 'name']

#joined_str = ' '.join(example_list)
#print(joined_str)
#example dashed name


#int_1 = 4
#int_2 = 2

#print(int_1 ** int_2)


#Which of the following functions is used to count the times a substring appears in a string?
#Answer: count()


#What Are Lists and How Do They Work?

#cities = ['Los Angeles', 'London', 'Tokyo']
#cities[0]
#print(cities[-1])

#dev = 'Zhyrus'
#list(dev)
#print(list(dev))

#num = [1, 2, 3, 4, 5]
#len(num)
#print(len(num))


#prolang = ['Python', 'Java', 'C++', 'JavaScript']
#del prolang[2]
#print(prolang)

#'C++' in prolang
#'JavaScript' in prolang


dev = ['Zhyrus', 27, ['Naomi', 'John']]

dev[2][0]
print(dev[2][0])


dev1 = ['Zhyrus', 27, 'Python Developer']
name, age, occupation = dev1
print(name,age,occupation)

dev3 = ['Zhyrus', 27, 'Python Developer']
name, *rest = dev3

print(name)
print(rest)

dess = ['cake', 'ice cream', 'cookies', 'brownies', 'pie']
dess[1:4]
print(dess[1:4])


numbers = [1, 2, 3, 4, 5, 6]
numbers[1:2]
print(numbers[1::2])