# Exercise 1.2. Write Python code to evaluate these expressions.
# The answers can be stored in a name, or evaluated in a print statement

# 1. How many seconds are there in 42 minutes 42 seconds?

x = ((42 * 60) + 42)
print(x)

min = 42
sec = 42

totalsec = ((min * 60) + sec)
print(totalsec)


# 2. How many miles are there in 10 kilometers? Hint: there are 1.61
# kilometers in a mile.

kilometers = 10
miles = kilometers / 1.61
print(miles)


# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your
# average pace (time per mile in minutes and seconds)? What is your average
# speed in miles per hour?



race_min = 42
race_sec = 42
kilo_distance = 10

miles_distance = kilo_distance * 0.621371
total_time_min = race_min + race_sec / 60

#pace per the mile
avg_miles_min = total_time_min / miles_distance

#min and sec conversion
avg_min = int(avg_miles_min)
avg_sec = int((avg_miles_min - avg_min) * 60)

#mph calculation
avg_speed = miles_distance / (total_time_min / 60)







