#Define the variables
hours = 2
minutes_in_an_hour = 60 #How many minutes that make a hour
seconds_in_a_minute = 60 # Number of seconds in a minute

#Perform the conversion of hours to minutes
minutes_to_seconds = minutes_in_an_hour * seconds_in_a_minute #This is the conversion of minutes to seconds
seconds = hours * minutes_to_seconds #This is the conversion of hours to seconds

#Display the results
print(f'{hours} hour(s) is {seconds} seconds')

