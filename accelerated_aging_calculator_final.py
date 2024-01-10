import math
import datetime

def get_calculator_type():
    while True:
        calculator_type = input("\nEnter either 'Accelerated' or 'Target' from the options above to proceed: ")
        if calculator_type.lower() == "accelerated" or calculator_type.lower() == "target":
            return calculator_type
        else:
            print("\nPlease enter a valid calculator type: 'Accelerated' or 'Target'.")

def get_int_input(user_prompt):
    while True:
        try:   
            return int(input(user_prompt))
        except ValueError:
            print("Please enter a valid numeric value.")

def get_float_input(user_prompt):
    while True:
        try:   
            return float(input(user_prompt))
        except ValueError:
            print("Please enter a valid numeric value.")

def get_date_input(user_prompt):
    while True:
        try:   
            return datetime.datetime.strptime(input(user_prompt), "%d/%m/%Y").date()
        except ValueError:
            print("Please enter a valid date.")

def accelerated(target_shelf_life, aging_temp, realtime_temp, q10):
    accelerated_factor = round(math.pow(q10, (aging_temp - realtime_temp) / 10), 2)
    accelerated_aging = round(target_shelf_life / math.pow(q10, (aging_temp - realtime_temp) / 10))
    return accelerated_aging, accelerated_factor

def target(num_of_days_staged, aging_temp, realtime_temp, q10):
    accelerated_factor = round(math.pow(q10, (aging_temp - realtime_temp) / 10), 2)
    shelf_life_achieved = round(num_of_days_staged * math.pow(q10, (aging_temp - realtime_temp) / 10))
    return shelf_life_achieved, accelerated_factor

# This section asks what calculator type you want to use.
print("""\nAccelerated\t- to calculate the number of Real-time Days needed to stage the product to reach Target Shelf Life at the Accelerated Aging Temperature.
Target\t\t- to calculate the Target Shelf Life achieved based on the number of Real-time days of staging completed. """)

calculator_type = get_calculator_type()
if calculator_type.lower() == "accelerated":

# Asks user for input      
    shelf_life = get_int_input("Target Shelf Life (Days): ")
    aging_temp = get_int_input("Accelerated Aging Temperature (TAA) for the protocol (\N{DEGREE SIGN}C): ")
    realtime_temp = get_int_input("Real-time Ambient Shelf Temperature (TRT) for the protocol (\N{DEGREE SIGN}C): ")
    q10 = get_float_input("Q10 Value for the protocol (e.g., 2.0):  ")
    start_date = get_date_input("Date you would like to start staging the product (DD/MM/YYYY): ")

# This section works out the number of days the product need to be staged for from user input.
    accelerated_aging, accelerated_factor = accelerated(shelf_life, aging_temp, realtime_temp, q10)
    staging_removal_date = start_date + datetime.timedelta(accelerated_aging)

    print(f"""\n------------
The Target Shelf Life for the product is:\t {shelf_life} Days
Accelerated Aging Temperature (TAA):\t\t {aging_temp}\N{DEGREE SIGN}C
Real-time Ambient Shelf Temperature (TRT):\t {realtime_temp}\N{DEGREE SIGN}C
Q10 Value:\t\t\t\t\t {q10}
Accelerated Aging Factor (AAF):\t\t\t {accelerated_factor}
------------

The product will need to be staged for: {accelerated_aging} Days
Just to note, the number of days needed to stage the product is rounded to the nearest whole day.

------------
Start Date for Staging Product: {start_date.strftime("%d/%m/%Y")}
Removal Date for Staging Product: {staging_removal_date.strftime("%d/%m/%Y")}""")
    
elif calculator_type.lower() == "target":

# Asks user for input  
    num_of_days_staged = get_int_input("Number of Real-time days completed of staging the product: ")
    aging_temp = get_int_input("Accelerated Aging Temperature (TAA) for the protocol (\N{DEGREE SIGN}C): ")
    realtime_temp = get_int_input("Real-time Ambient Shelf Temperature (TRT) for the protocol (\N{DEGREE SIGN}C): ")
    q10 = get_float_input("Q10 Value for the protocol (e.g., 2.0):  ")

# This section works out the number of days the product has been staged for in real time based off accelerated conditions.
    shelf_life_achieved, accelerated_factor_1 = target(num_of_days_staged, aging_temp, realtime_temp, q10)
    print(f"""\n------------
The Real-time Days the product has been staged for is:\t\t {num_of_days_staged} Days
Accelerated Aging Temperature (TAA):\t\t\t\t {aging_temp}\N{DEGREE SIGN}C
Real-time Ambient Shelf Temperature (TRT):\t\t\t {realtime_temp}\N{DEGREE SIGN}C
Q10 Value:\t\t\t\t\t\t\t {q10}
Accelerated Aging Factor (AAF):\t\t\t\t\t {accelerated_factor_1}
------------

The Target Shelf Life achieved so far for the product is: {shelf_life_achieved} Days
Just to note, the number of days of your target shelf life achieved so far is rounded to the nearest whole day. """)
    
