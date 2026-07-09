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


name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade








