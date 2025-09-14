#Define the variables
hours = 2
minutes_in_an_hour = 60 #How many minutes that make a hour
seconds_in_a_minute = 60 # Number of seconds in a minute

#Perform the conversion of hours to minutes
conversion1 = hours * minutes_in_an_hour #This will convert the 2 hours into minutes
seconds = conversion1 * seconds_in_a_minute #This is the end product of the conversion from hours to seconds

#Display the results
print(f'{hours} hour(s) is {seconds} seconds')

