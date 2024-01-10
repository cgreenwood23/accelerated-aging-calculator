import math
import datetime

print("""\nAccelerated\t- to calculate the number of Real-time Days needed to stage the product to reach Target Shelf Life at the Accelerated Aging Temperature.
Target\t\t- to calculate the Target Shelf Life achieved based on the number of Real-time days of staging completed. """)

calculator_type = input("\nEnter either 'Accelerated' or 'Target' from the options above to proceed: ")

if calculator_type.lower() == "accelerated":
    accelerated_target_shelf_life = int(input("Target Shelf Life (Days): "))
    accelerated_aging_temp = int(input("Accelerated Aging Temperature (TAA) for the protocol (\N{DEGREE SIGN}C): "))
    accelerated_realtime_temp = int(input("Real-time Ambient Shelf Temperature (TRT) for the protocol (\N{DEGREE SIGN}C): "))
    accelerated_q10 = float(input("Q10 Value for the protocol (e.g., 2.0):  "))
    staging_start_date = datetime.datetime.strptime(input("Date you would like to start staging the product (DD/MM/YYYY): "), "%d/%m/%Y").date()

    accelerated_factor = math.pow(accelerated_q10, (accelerated_aging_temp - accelerated_realtime_temp) / 10)
    rounded_accelerated_factor = round(accelerated_factor, 2)
    accelerated_aging = accelerated_target_shelf_life / math.pow(accelerated_q10, (accelerated_aging_temp - accelerated_realtime_temp) / 10)
    rounded_accelerated_aging = round(accelerated_aging, 0)
    staging_removal_date = staging_start_date + datetime.timedelta(rounded_accelerated_aging)
    print(f"""\n------------
The Target Shelf Life for the product is:\t {accelerated_target_shelf_life} Days
Accelerated Aging Temperature (TAA):\t\t {accelerated_aging_temp}\N{DEGREE SIGN}C
Real-time Ambient Shelf Temperature (TRT):\t {accelerated_realtime_temp}\N{DEGREE SIGN}C
Accelerated Aging Factor (AAF):\t\t\t {rounded_accelerated_factor}
Q10 Value:\t\t\t\t\t {accelerated_q10}
------------

The product will need to be staged for: {rounded_accelerated_aging} Days
Just to note, the number of days needed to stage the product is rounded to the nearest whole day.

------------
Start Date for Staging Product: {staging_start_date.strftime("%d/%m/%Y")}
Removal Date for Staging Product: {staging_removal_date.strftime("%d/%m/%Y")} """)

elif calculator_type.lower() == "target":
    num_of_days_staged = int(input("Number of Real-time days completed of staging the product: "))
    target_aging_temp = int(input("Accelerated Aging Temperature (TAA) for the protocol (\N{DEGREE SIGN}C): "))
    target_realtime_temp = int(input("Real-time Ambient Shelf Temperature (TRT) for the protocol (\N{DEGREE SIGN}C): "))
    target_q10 = float(input("Q10 Value for the protocol (e.g., 2.0):  "))

    accelerated_factor_1 = math.pow(target_q10, (target_aging_temp - target_realtime_temp) / 10)
    rounded_accelerated_factor_1 = round(accelerated_factor_1, 2)
    shelf_life_achieved = num_of_days_staged * math.pow(target_q10, (target_aging_temp - target_realtime_temp) / 10)
    rounded_shelf_life_achieved = round(shelf_life_achieved, 0)
    print(f"""\n------------
The Real-time Days the product has been staged for is:\t\t {num_of_days_staged} Days
Accelerated Aging Temperature (TAA):\t\t\t\t {target_aging_temp}\N{DEGREE SIGN}C
Real-time Ambient Shelf Temperature (TRT):\t\t\t {target_realtime_temp}\N{DEGREE SIGN}C
Accelerated Aging Factor (AAF):\t\t\t\t\t {rounded_accelerated_factor_1}
Q10 Value:\t\t\t\t\t\t\t {target_q10}
------------

The Target Shelf Life achieved so far for the product is: {rounded_shelf_life_achieved} Days
Just to note, the number of days of your target shelf life achieved so far is rounded to the nearest whole day.""")

else:
    print("\nPlease enter a valid calculator type: 'Accelerated' or 'Target'.")
