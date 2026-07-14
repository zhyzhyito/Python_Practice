#transpo = input("Chose Vihicle:")

#if transpo == "Motorcycle":
#    print("Pay for motorcycle 50php")
#elif transpo == "Car":
#    print("Pay for car 100")
#elif transpo == "Truck":
#    print("Pay for truck 100")
#else:
#    print("Vihicle not register")

#prices, transpo = {"Motorcycle": 50, "Car": 100, "Truck": 200}, input("Chose Vehicle: ")
#print(f"Pay: {prices.get(transpo, 'Vehicle not registered')}")



#typeofvihicle = input("What type of vihicle you use?: ").lower()

#if typeofvihicle == "scooter":
#    print("Recommend Oil Scooter: 10w-30")
#elif typeofvihicle == "underbone":
#    print("Recommended Oil: 10w-40 ")
#elif typeofvihicle == "bigbike":
#    print("Recommended Oil Fully Synthetic: 10w-50")

#else:
#    print("No found oil for your vihicle")


#for i in range(5,0, -1):
#    print(i)
#    print("GO!")

#for i in range(51,0, + 5):
#   print(i)

#serial = "FIFIFURIOUS"

#for i in serial:

#    if i == "F":

#        print("Fi Component Detected!")

#startnum, kilo = 0, "kilo-kilokilo-kilo"

#for i in kilo:
#    if i == "k":
#        startnum += 1
#print(f"Total kilo is : {startnum} kl")


#sprocket_price , chain_price = 450 , 350

#total_cost = chain_price + sprocket_price

#print(total_cost)


#ALL DATA TYPES

#my_integer_var = 10
#print(type(my_integer_var))  # <class 'int'>

##my_float_var = 4.50
#print(type(my_float_var))  # <class 'float'>

#my_string_var = 'hello'
#print(type(my_string_var))  # <class 'str'>

#my_boolean_var = True
#print(type(my_boolean_var))  # <class 'bool'>

#my_set_var = {7, 'hello', 8.5}
#print(type(my_set_var))  # <class 'set'>

#my_dictionary_var = {'name': 'Alice', 'age': 25}
#print(type(my_dictionary_var))  # <class 'dict'>

#my_tuple_var = (7, 'hello', 8.5)
#print(type(my_tuple_var))  # <class 'tuple'>

#my_range_var = range(5)
#print(type(my_range_var))  # <class 'range'>

#my_list = [22, 'Hello world', 3.14, True]
#print(type(my_list)) # <class 'list'>

#my_none_var = None
#print(type(my_none_var))  # <class 'NoneType'>


#acount = '12'

#isinstance(acount, (int, float))

#msg2 = "Helloworld"

#print(msg2[5])
#print(msg2[6])

#greet = 'hello'
#greet = 'hi'

#print(greet)

#msg3 = 'hi'
#msg4 = 'poww'

#com = msg3 + ' ' +msg4
#print(com)

#my_int_1 = 56
#my_int_2 = 12

#my_float_1 = 5.4
#my_float_2 = 12.0

#mod_ints = my_int_1 % my_int_2
#mod_floats = my_float_2 % my_float_1

#print('Integer Modulo:', mod_ints) # Integer Modulo: 8
#print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993

#my_int_1 = 56
#my_int_2 = 12

#my_float_1 = 5.4
#my_float_2 = 12.0

#floor_div_ints = my_int_1 // my_int_2
#floor_div_floats = my_float_2 // my_float_1

#print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
#print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0

#greet = 'Hello'
#greet *= 3

#print(greet) # HelloHelloHello
#my_var = 5

#print(+my_var)   # 5
#print(++my_var)  # 5
#print(+++my_var) # 5

#my_var += 1
#print(my_var) # 6



# How Do Conditional Statements and Logical Operators Work?\
#print(3 > 4) # False
#print(3 < 4) # True
#print(3 == 4) # False
#print(4 == 4) # True
#print(3 != 4) # True
#print(3 >= 4) # False
#print(3 <= 4) # True

#age = 18

#if age >= 18:
#    print('ADULT!')

#elif age >= 13:
#    print('TEENAGER')
#elif age >= 18:
#    print('ADULT')
#else:
#    print('NOT TODAY')

#THIS IS HOW TO USE NESTED CONDITIONAL LOOP

#VoterIsADULT = True
#age = 18

#if VoterIsADULT and age >= 18:
#        print('You are a VOTER!')
#else:
#    print('You are not VOTER')

#age1 = 120
#employed = True

#if age1 < 120 or employed:
#    print('NICE')
#else:
#    print('NOT NICE')


#is_citizen = True
#age = 25
#if is_citizen:
#    if age >= 18:
#        print('VOTE!')
#    else:
#        print('DO NOTE VOTE!')


#is_admin = False
#if not is_admin:
#    print('Access Dedined')
#else:
#    print('Access Granted')


#is_admin = True
#if not is_admin:
#    print('Access Dedined')
#else:
#    print('Access Granted')


#Q1: What will the following code output?
#age = 20
#has_ticket = True

#if age >= 18 and has_ticket:
#    print("You can watch the movie.")
#else:
#    print("You can't watch the movie.")

    #Answer: 'You can watch the movie'

#Q2: Which of the following is NOT considered a falsy value in Python?

    #Answer: 'False'

#3: What happens when Python evaluates the expression x or y?

    #Answer: It returns x if it evaluates to True,-
    # and skips evaluating y

#---------------------------

#How Do Functions Work in Python?
#Functions are reusable pieces of code 
#that run when you call them. Many programming languages 
#come with built-in functions that make it easier to get started. 
#Python is no exception, and we've already covered some built-in 
#functions like print() in previous lessons.

#Another helpful built-in function is input(), 
#which lets you prompt the user for input:


#name = input('What is your name?')
#print('Hello', name)

#print(int(3.14)) # 3
#print(int('42')) # 42
#print(int(True)) # 1
#print(int(False)) # 0 

#rint( 'Hi' )


#def calculate_sum(a, b):
#    return(a + b)

#my_sum = calculate_sum(3,1)
#print(my_sum)

#What Is Scope in Python and How Does It Work?


#To correctly determine scope, Python follows the LEGB rule, which stands for the following:

#Local scope (L): Variables defined in functions or classes.

#Enclosing scope (E): Variables defined in enclosing or nested functions.

#Global scope (G): Variables defined at the top level of the module or file.

#Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.

#def my_func():
#    my_var = 10
#    print(my_var)

#my_func()

#print(my_var)


#def outer_func():
#    msg = 'Hello there!'
#    res = ""

#    def inner_func():
#        nonlocal res
#        res = 'How are you?'
#        print(msg)

#    inner_func()
#    print(res)

#outer_func()


#my_var = 100

#def show_var():
#    print(my_var)

#show_var()
#print(my_var)

#my_var_1 = 7

#def show_vars():
#    global my_var_2
#    my_var_2 = 10
#    print(my_var_1)
#    print(my_var_2)

#show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
#print(my_var_2) # 10


#my_var = 10  # A global variable

#def change_var():
#    global my_var  # Allows modification of a global variable
#    my_var = 20

#change_var()

#print(my_var)  # my_var is now modified globally to 20


#print(str(45)) # '45'
#print(type(3.14)) # <class 'float'>
#print(isinstance(3, str)) # False

#def apply_discount(price, discount):
    # 1. Check kung numero ang price
#    if not isinstance(price, (int, float)):
#        return "The price should be a number."
    
    # 2. Check kung numero ang discount
#    if not isinstance(discount, (int, float)):
#        return "The discount should be a number."
    
    # 3. Check kung valid ang range ng price
#    if price <= 0:
#        return "The price should be greater than 0."
    
    # 4. Check kung valid ang range ng discount
#    if discount < 0 or discount > 100:
#        return "The discount should be between 0 and 100."
    
    # Ibabawas ang discount amount sa orihinal na price
#    final_price = price - (price * (discount / 100))
#    return final_price
        
#def caesar(text, shift, encrypt=True):

#    if not isinstance(shift, int):
#        return 'Shift must be an integer value.'
#    if shift < 1 or shift > 25:
#        return 'Shift must be an integer between 1 and 25.'
#    if not encrypt:
#        shift = -shift

#    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

#    return text.translate(translation_table)

#def encrypt(text, shift):
#    return caesar(text, shift, encrypt=True)

#def decrypt(text, shift):
#    return caesar(text, shift, encrypt=False)


#encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf'
#decrypted_text = decrypt(encrypted_text, 3)
#print(encrypted_text)



##_________________________________________

"""""Character Creation Function
The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
The character name should be validated:"""

#full_dot = '●'
#empty_dot = '○'

#def create_character(name, strength, intelligence, charisma):
#    if not isinstance(name, str):
#        return "The character name should be a string."
#    if name == "":
#        return "The character should have a name."
#    if len(name) > 10:
#        return "The character name is too long."
#    if " " in name:
#        return "The character name should not contain spaces."
    
#    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
#        return "All stats should be integers."
#    if strength < 1 or intelligence < 1 or charisma < 1:
#        return "All stats should be no less than 1."
#    if strength > 4 or intelligence > 4 or charisma > 4:
#        return "All stats should be no more than 4."
#    if strength + intelligence + charisma != 7:
#        return "The character should start with 7 points."

#    return f"{name}\nSTR {full_dot * strength}{empty_dot * (10 - strength)}\nINT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\nCHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    

#The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
#The character name should be validated:
#If the character name is not a string, the function should return The character name should be a string.
#If the character name is an empty string, the function should return The character should have a name.
#If the character name is longer than 10 characters, the function should return The character name is too long.
#If the character name contains spaces, the function should return The character name should not contain spaces.


#The stats should also be validated:
#If one or more stats are not integers, the function should return All stats should be integers.
#If one or more stats are less than 1, the function should return All stats should be no less than 1.
#If one or more stats are more than 4, the function should return All stats should be no more than 4.
#If the sum of all stats is different than 7, the function should return The character should start with 7 points.
#If all values pass the verification, the function should return a string with four lines:
#the first line should contain the character name
#lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.
#Here's the string that should be returned by create_character('ren', 4, 2, 1):

#ren
#STR ●●●●○○○○○○
#INT ●●○○○○○○○○
#CHA ●○○○○○○○○○
#NOTE: while str and int are common abbreviations for the stats, remember that those are reserved keywords in Python and should not be used as variable names.



##_________________________________________




#Python Basics Review
#What is Python?
#Introduction: Python is a general-purpose programming language known for its simplicity and ease of use. Python is used in many fields like data science and machine learning, web development, scripting and automation, embedded systems and IoT, and much more.
#Common Use Cases: Python is used in data science, machine learning, web development, cybersecurity, automation and microcomputers like the Raspberry Pi and MicroPython-compatible boards.
#Variables
#Declaring Variables: To declare a variable, you start with the variable name followed by the assignment operator (=) and then the value. This can be a number, string, boolean, etc. Here are some examples:
name = 'John Doe'
age = 25
#Naming Conventions for Variables: Here are the naming conventions you should use for variables:

#Variable names can only start with a letter or an underscore (_), not a number.
#Variable names can only contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
#Variable names are case-sensitive — age, Age, and AGE are all considered unique.
#Variable names cannot be one of Python’s reserved keywords such as if, class, or def.
#Variables names with multiple words are separated by underscores. Ex. snake_case.
#Comments
#Single Line Comments: These types of comments should be used for short notes you wish to leave in your code.
# This is a single line comment
#Multi-line Strings: These types of strings can be used to leave larger notes or to comment out sections of code.
"""
This is a multi-line string.
Here is some code commented out.

name = 'John Doe'
age = 25
"""
#print() Function: To print data to the console, you can use the print() function like this:
#print('Hello world!') # Hello world!
#Common Data Types in Python
#Introduction: Python is a dynamically-typed language like JavaScript, meaning you don't need to explicitly declare types for variables. The language knows what the type of a variable is based on what you assign to the variable.
#Integer: A whole number without decimals:
#my_integer_var = 10
#print('Integer:', my_integer_var) # Integer: 10
#Float: A number with decimals:
#my_float_var = 4.50
#print('Float:', my_float_var) # Float: 4.5
#String: A sequence of characters wrapped in quotes:
#my_string_var = 'hello'
#print('String:', my_string_var) # String: hello
#Boolean: A value representing either True or False:
#my_boolean_var = True
#print('Boolean:', my_boolean_var) # Boolean: True
#Set: An unordered collection of unique elements:
#my_set_var = {7, 5, 8}
#print('Set:', my_set_var) # Set: {7, 5, 8}
#Dictionary: A collection of key-value pairs, enclosed in curly braces:
#my_dictionary_var = {"name": "Alice", "age": 25}
#print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
#Tuple: An immutable ordered collection, enclosed in parentheses:
#my_tuple_var = (7, 5, 8)
#print('Tuple:', my_tuple_var) # Tuple: (7, 5, 8)
#Range: A sequence of numbers, often used in loops:
#my_range_var = range(5)
#print(my_range_var) # range(0, 5)
#List: An ordered collection of elements that supports different data types:
#my_list = [22, 'Hello world', 3.14, True]
#print(my_list) # [22, 'Hello world', 3.14, True]
#None: A special value that represents the absence of a value:
#my_none_var = None
#print('None:', my_none_var) # None: None
#Immutable and Mutable Types
#Immutable Types: These types cannot change once declared, although you can point their variables at something new, which is called reassignment. They include integer, float, complex, boolean, string, tuple, range, and None.
#Mutable Types: These types can change once declared. You can add, remove, or update their items. They include collection types such as list, set, and dictionary.
#type() Function: To see the type for a variable, you can use the type() function like this:
#greeting = 'Hello there!'
#age = 21

#print(type(greeting)) # <class 'str'>
#print(type(age)) # <class 'int'>
#isinstance() Function: This is used to check if a variable matches a specific data type:
greeting = 'Hello world'
name = 'John Doe'

print(isinstance(greeting, str)) # True
print(isinstance(name, int)) # False
#Working with Strings
#Definition: As you recall from JavaScript, strings are immutable which means you can not change them after they have been created. In Python, you can use either single or double quotes. It is recommended to choose a rule and stick with it:
developer = 'Jessica'
city = "Los Angeles"
#Accessing Characters from Strings: You can access characters from strings by using bracket notation like this:
my_str = 'Hello world'

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l
#Escaping Strings: You can use a backslash (\) if your string contains quotes like this:
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
#String Concatenation: To concatenate strings, you can use the + operator like this:
developer = 'Jessica'
print('My name is ' + developer + '.') # My name is Jessica.
#Another way to concatenate strings is by using the += operator. This is used to perform concatenation and assignment in the same step like this:

greeting = 'My name is '
developer = 'Jessica.'

greeting += developer
print(greeting) # My name is Jessica.
#f-strings: This is short for formatted string literals. It allows you to handle interpolation and also do some concatenation with a compact and readable syntax:
developer = 'Jessica'
greeting = f'My name is {developer}.'
print(greeting) # My name is Jessica.
#String Slicing: This is when you can extract portions of a string. Here is the basic syntax:
#str[start:stop:step]
#The start position represents the index where the extraction should begin. The stop position is where the slice should end. This position is non inclusive. The step position represents the interval to increment for the slicing. Here are some examples:

message = 'Python is fun!'

print(message[0:6])  # Python
print(message[7:])  # is fun!
print(message[::2])  # Pto sfn
#Getting the Length of a String: The len() function is used to return the number of the characters in the string:
developer = 'Jessica'

print(len(developer)) # 7
#Working with the in operator
#in Operator: This returns a boolean that specifies whether the character or characters exist in the string or not:
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
#Common String Methods
#str.upper(): This returns a new string with all characters converted to uppercase:
developer = 'Jessica'

print(developer.upper()) # JESSICA
#str.lower(): This returns a new string with all characters converted to lowercase:
developer = 'Jessica'

print(developer.lower()) # jessica
#str.strip(): This returns a copy of the string with specified leading and trailing characters removed (if no argument is passed to the method, it removes leading and trailing whitespace).
greeting = '  hello world  '

trimmed_my_str = greeting.strip()
print(trimmed_my_str)  # 'hello world'
#replace(): This returns a new string with all occurrences of the old string replaced by a new one.
greeting = 'hello world'

replaced_my_str = greeting.replace('hello', 'hi')
print(replaced_my_str)  # 'hi world'
#split(): This is used to split a string into a list using a specified separator. A separator is a string specifying where the split should happen.
dashed_name = 'example-dashed-name'

split_words = dashed_name.split('-')
print(split_words)  # ['example', 'dashed', 'name']
#join(): This is used to join elements of an iterable into a string with a separator. An iterable is a collection of elements that can be looped over like a list, string or a tuple.
example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(joined_str)  # example dashed name
#str.startswith(prefix): This returns a boolean indicating if a string starts with the specified prefix:
developer = 'Naomi'

result = developer.startswith('N')
print(result)  # True
#str.endswith(suffix): This returns a boolean indicating if a string ends with the specified suffix:
developer = 'Naomi'

result = developer.endswith('N')
print(result)  # False
#str.find(): This returns the index for the first occurrence of a substring. If one is not found, then -1 is returned:
developer = 'Naomi'

result = developer.find('N')
print(result)  # 0

city = 'Los Angeles'
print(city.find('New')) # -1
#str.count(substring): This counts how many times a substring appears in a string:
city = 'Los Angeles'
print(city.count('e')) # 2
#str.capitalize(): This returns a new string with the first character capitalized and the other characters lowercased:
dessert = 'chocolate cake'
print(dessert.capitalize()) # Chocolate cake
#str.isupper(): This returns True if all letters in the string are uppercase and False if otherwise:
dessert = 'chocolate cake'
print(dessert.isupper()) # False
#str.islower(): This returns True if all letters in the string are lowercase and False if otherwise:
dessert = 'chocolate cake'
print(dessert.islower()) # True
#str.title(): This returns a new string with the first letter of each word capitalized:
city = 'los angeles'
print(city.title()) # Los Angeles
#str.maketrans(): This method is used to create a table of 1 to 1 character mappings for translation. It is often used with the translate() method which applies that table to a string and return the translated result.
trans_table = str.maketrans('abc', '123')
print(trans_table) # {97: 49, 98: 50, 99: 51}

result = 'abcabc'.translate(trans_table)
print(result)  # 123123
#Common Operations used with Integers and Floats
#Basic Math Operations: In Python, you can do basic math operations with integers and floats including addition, subtraction, multiplication and division:
int_1 = 56
int_2 = 12
float_1 = 5.4
float_2 = 12.0

# Addition

print('Integer Addition:', int_1 + int_2) # Integer Addition: 68
print('Float Addition:', float_1 + float_2) # Float Addition: 17.4

# Subtraction

print('Int Subtraction:', int_1 - int_2) # Int Subtraction: 44
print('Float Subtraction:',  float_2 - float_1) # Float Subtraction: 6.6

# Multiplication

print('Int Multiplication:', int_1 * int_2) # Int Multiplication: 672
print('Float Multiplication:', float_2 * float_1) # Float Multiplication: 64.80000000000001

# Division

print('Division:', int_1 / int_2) # Division: 4.666666666666667
print('Float Division:', float_2 / float_1) # Float Division: 2.222222222222222
#When you add a float and an integer, the result will be converted to a float like this:

int_1 = 56
float_1 = 5.4

print(int_1 + float_1) # 61.4
#Modulo Operator (%): This returns the remainder when a number is divided by another number:
int_1 = 56
int_2 = 12

print(int_1 % int_2) # 8
#Floor Division (//): This operator is used to divide two numbers and round down the result to the nearest whole number:
int_1 = 56
int_2 = 12

print(int_1 // int_2) # 4
#Exponentiation Operator (**): This operator is used to raise a number to the power of another:
int_1 = 4
int_2 = 2

print(int_1 ** int_2) # 16
#float() Function: You can use this function to convert an integer to float.
num = 4

print(float(num)) # 4.0
#int() Function: You can use this function to convert an float to an integer.
num = 4.0

print(int(num)) # 4
#round() Function: This is used to round a number to the nearest whole integer:
num_1 = 3.4
num_2 = 7.7

print(round(num_1)) # 3
print(round(num_2)) # 8
#abs() Function: This is used to return the absolute value of a number:
num = -13

print(abs(num)) # 13
#pow() Function: This is used to raise a number to the power of another:
result = pow(2, 3) 
print(result)  # 8
#Augmented Assignments
#Definition: Augmented assignment combines a binary operation with an assignment in one step. It takes a variable, applies an operation to it with another value, and stores the result back into the same variable.
# Addition assignment 
my_var = 10
my_var += 5

print(my_var) # 15

# Subtraction assignment
count = 14
count -= 3

print(count) # 11

# Multiplication assignment 
product = 65
product *= 7

print(product) # 455

# Division assignment 
price = 100
price /= 4

print(price) # 25.0

# Floor Division assignment 
total_pages = 23
total_pages //= 5

print(total_pages) # 4

# Modulo assignment 
bits = 35
bits %= 2

print(bits) # 1

# Exponentiation assignment 
power = 2
power **= 3

print(power) # 8
#There are other augmented assignment operators too, like those for bitwise operators. They include &=, ^=, >>=, and <<=.

#Working with Functions
#Definition: Functions are reusable pieces of code that take inputs (arguments) and returns an output. To call a function, you need to reference the function name followed by a set of parenthesis:
# Defining a function

def get_sum(num_1, num_2):
    return num_1 + num_2

result = get_sum(3, 4) # function call
print(result) # 7
#If a function does not explicitly return a value, then the default return value is None:

def greet():
    print('hello') 

result = greet() # hello
print(result) # None
#You can also supply default values to parameters like this:

def get_sum(num_1, num_2=2):
    return num_1 + num_2

result = get_sum(3) 
print(result) # 5
#If you call the function without the correct number of arguments, you will get a TypeError:

def calculate_sum(a, b):
    print(a + b)

calculate_sum()

# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
#Common Built-in Functions
#input() Function: This is used to prompt the user for some input:
name = input('What is your name?') # User types 'Kolade' and presses Enter  
print('Hello', name) # Hello Kolade
#int() Function: This is used to convert a number, boolean, or a numeric string into an integer:
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 
#Scope in Python
#Local Scope: This is when a variable declared inside a function or class can only be accessed within that function or class.
def my_func():
    num = 10
    print(num)
#Enclosing Scope: This is when a function that's nested inside another function can access the variables of the function it's nested within.
def outer_func():
    msg = 'Hello there!'
    
    def inner_func():
        print(msg)
    inner_func()

print(outer_func()) # Hello there!
#Global Scope: This refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program.
tax = 0.70 

def get_total(subtotal):
    total = subtotal + (subtotal * tax)
    return total

print(get_total(100))  # 170.0
#Built-in Scope: Reserved names in Python for predefined functions, modules, keywords, and objects.
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
#Comparison Operators
#Equal (==): Checks if two values are equal:
print(3 == 4) # False
#Not equal (!=): Checks if two values are not equal:
print(3 != 4) # True
#Strictly greater than (>): Checks if one value is greater than another:
print(3 > 4) # False
#Strictly less than (<): Checks if one value is less than another:
print(3 < 4) # True
#Greater than or equal(>=): Checks if one value is greater than or equal to another:
print(3 >= 4) # False
#Less than or equal(<=): Checks if one value is less than or equal to another:
print(3 <= 4) # True
#Working with if, elif and else Statements
#if Statements: These are conditions used to determine if something is true or not. If the condition evaluates to True, then that block of code will run.
age = 18

if age >= 18:
    print('You are an adult') # You are an adult
#elif Clause: These are conditions that come after an if statement. An elif clause runs only if all previous conditions evaluate to False and its own condition evaluates to True.
age = 16

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')  # You are a teenager
#else Clause: This will run if no other conditions evaluate to True.
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')  # You are a child
#You can also use nested if statements like this:

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
#Truthy and Falsy Values
#Definition: In Python, every value has an inherent boolean value, or a built-in sense of whether it should be treated as True or False in a logical context. Many values are considered truthy, that is, they evaluate to True in a logical context. Others are falsy, meaning they evaluate to False. Here are some examples of falsy values:
None
False
#Integer 0
#Float 0.0
#Empty strings ''
#Other values like non-zero numbers, and non-empty strings are truthy.

#Working with the bool() Function
#Definition: If you want to check whether a value is truthy or falsy, you can use the built-in bool() function. It explicitly converts a value to its boolean equivalent and returns True for truthy values and False for falsy values. Here are a few examples:
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
#Boolean Operators and Short-circuiting
#Definition: These are special operators that allow you to combine multiple expressions to create more complex decision-making logic in your code. There are three Boolean operators in Python: and, or, and not.
#and Operator: This operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value.
is_citizen = True
age = 25

print(is_citizen and age) # 25
#You can also use the and operator in conditionals like this:

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
#or Operator: This operator returns the first operand if it is truthy, otherwise, it returns the second operand. An or expression results in a truthy value if at least one operand is truthy. Here is an example:
age = 19
is_employed = False

print(age or is_employed) # 19
#Just like with the and operator, you can use the or operator in conditionals like this:

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
#Short-circuiting: The and and or operators are known as a short-circuit operators. Short-circuiting means Python checks values from left to right and stops as soon as it determines the final result.
#not Operator: This operator takes a single operand and inverts its boolean value. It converts truthy values to False and falsy values to True. Unlike the previous operators we looked at, not always returns True or False. Here are some examples:
print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy
#Here is an example of the not operator in a conditional:

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

