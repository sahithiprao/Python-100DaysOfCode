print("Welcome to the tip calculator")
total_amt = input("What was the total bill? ")
tip_percentage = input("How much tip would you like to give? 10, 12, 0r 15? ")
split_num = input("How many people to split the bill? ")
total_int_amt = float(total_amt)
total_int_amt += total_int_amt * (float(tip_percentage)/100)
total_split_amt = round(total_int_amt/int(split_num),2) # sometimes 0 in th end is not exactly printed
total_split_amt = "{:.2f}".format(total_int_amt)# this will round off 2 decimals
print(f"Each person should pay: {total_split_amt}")