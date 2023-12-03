# TODO: Create a converter that takes in degrees in Fahrenheit, and prints
# them out in celsius. Use the `input()` function to assist you.
# use documentation and your knowledge of Python to complete this

# consider: what happens if the `input()` function takes in a
# non-numeric answer. How will you handle erroneous values?

fahren = float(input("Enter Farenheit temp:"))
cels = (fahren - 32)/1.8
print(str(fahren)+ " Fahrenheit input is equivalent to\
 " + str(cels) + " degrees Celsius.")