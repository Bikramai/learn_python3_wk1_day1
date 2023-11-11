#variables
# 1.Update the variable meal to reflect each meal of the day before we print it.

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"
print('\n')

# Printing out breakfast
print("Breakfast:")
print(meal)
print('\n')

# Now update meal to be lunch!
meal = "rice and soup"
print('\n')

# Printing out lunch
print("Lunch:")
print(meal)
print('\n')

# Now update "meal" to be dinner
lunch = "rice and vegan soup"

# Printing out dinner
print("Dinner:")
print(meal)

#2. writing Python are SyntaxError and NameError.
# print('This message has mismatched quote marks!")
# print('\n')

# writing Python are NameError
# print(Abracadabra)
# print('\n')


# A recent movie-going experience has you excited to publish a review. You rush out of the cinema and hastily begin programming to create your movie-review website: The Big Screen’s Greatest Scenes Decided By A Machine.

# Create the following variables and assign integer numbers to them: release_year and runtime.

# Define the release and runtime integer variables below:
release_year = 1985
runtime = 130 

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 9.3

# 1.Print out the result of this equation: 25 * 68 + 13 / 28
sum=(25*68+13/28)
print(sum)
print('\n')

# 1.
# You’ve decided to get into quilting! To calculate the number of 
# squares you’ll need for your first quilt let’s create two 
# variables: quilt_width and quilt_length. Let’s make this 
# first quilt 8 squares wide and 12 squares long.

# Checkpoint 2 Passed
# 2.Print out the number of squares you’ll need to create the quilt!

# Checkpoint 3 Passed

# 3.It turns out that quilt required a little more material than you 
# have on hand! Let’s only make the quilt 8 squares long. How many 
# squares will you need for this quilt instead?
quilt_width = 8
quilt_length = 12

print(quilt_width*quilt_width)

quilt_length = 8
print(quilt_width*quilt_length)

# 1.You really like how the square 
# quilts from last exercise came out, 
# and decide that all quilts that you 
# make will be square from now on.

# Using the exponent operator, 
# print out how many squares you’ll 
# need for a 6x6 quilt, a 7x7 quilt, and an 8x8 quilt.
print(6*6)
print(7*7)
print(8*8)

# 2.Your 6x6 quilts have taken off so well, 6 people have each 
# requested 6 quilts. Print out how many tiles you would need 
# to make 6 quilts for each of the 6 people.
print(6*6*6*6)


# You are starting a new campaign for your online shop where every 11th customer gets 11% off of their next order. For ease, you decide that order numbers that are divisible by 11 will receive the coupon.

# Here comes order #263! Find the remainder by calculating 263 modulo 11 and store the result in a variable called order_263_r.

# Print out order_263_r.

# Checkpoint 2 Passed
# 2.
# Based on the value of order_263_r, should this order receive a coupon? Create a new variable called order_263_coupon and assign to it a value of "yes" if the order should get a coupon, otherwise "no".


# Stuck? Get a hint

# Checkpoint 3 Passed
# 3.
# Here comes another order, #264! Find the remainder by calculating 264 modulo 11 and store the result in a variable called order_264_r.

# Print out order_264_r.

# Checkpoint 4 Passed
# 4.
# Based on the value of order_264_r, should this order receive a coupon? Create a new variable called order_264_coupon and assign to it a value of "yes" if the order should get a coupon, otherwise "no".

order_263_r = 263 % 11
print(order_263_r)


order_263_coupon = "no"

order_264_r = 264 % 11
print(order_264_r)
order_264_coupon = "yes"

# Concatenation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 +string3+ string4+string5 +string6
print(message)

# Plus Equals


# We’re doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!

# Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.

# The prices (also included in the workspace) are:

new_sneakers = 50.00
nice_sweater = 39.00
fun_books = 20.00
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater + fun_books
print("The total price is", total_price)

# Multi-line Strings
# Assign the string here
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""

print(to_you)


# Create variables:

# my_age
# half_my_age
# greeting
# name
# greeting_with_name
# Assign values to each using your knowledge of division and concatenation!

# create variables
my_age = 37

half_my_age = 18.5

greeting = "Hello"

name = "Bikram"

greeting_with_name = print(f"{greeting}!, {name}")