# Exercise 1.1. It is a good idea to read this book in front of a computer so
# you can try out the examples as you go.

# Whenever you are experimenting with a new feature, you should try to make
# mistakes. For example, in the “Hello, world!” program, what happens if you
# leave out one of the quotation marks? What if you leave out both? What if
# you spell print wrong?

# This kind of experiment helps you remember what you read; it also helps when
# you are programming, because you get to know what the error messages mean.
# It is better to make mistakes now and on purpose than later and accidentally.

# 1. In a print statement, what happens if you leave out one of the
# parentheses, or both?

print("nice") #Getting syntax error that parenthesis wasn't closed


# 2. If you are trying to print a string, what happens if you leave out one
# of the quotation marks, or both?
print('ha') 
#Getting statement, "unterminated string literal"

# 3. You can use a minus sign to make a negative number like -2.
# What happens if you put a plus sign before a number? What about 2++2?

x = (2-+2) #When plus sign is added before number, the number remains positive, when + is added before number and after operation, the number following the + is treated like a positive number. Order of operations follows
print(x)

# 4. In math notation, leading zeros are ok, as in 09. What happens if you try
# this in Python?  What about 01

 #Message states "leading zeros in decimal integer"

# 5. What happens if you have two values with no operator between them? "22", "11"

x = 2211
print(x) #python sees "22" and "11" as one number, 2211

#Other Observations
#1. When there's one mistake, the terminal only shows the errors, no partially correct code