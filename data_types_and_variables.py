''' 5. You have rented some movies for your kids:
The Little Mermaid for 3 days
Brother Bear for 5 days
Hercules for 1 day
If the daily fee to rent a movie is 3 dollars, how much will you have to pay? '''
little_mermaid = 3
brother_bear = 5
hercules = 1
rental_cost = (little_mermaid + brother_bear + hercules) * 3
print('Rental cost')
print(rental_cost)

''' 6.
Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.
They pay you the following hourly rates:
Google: 400 dollars
Amazon: 380 dollars
Facebook: 350 dollars
This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
How much will you receive in payment for this week? '''
google = 400
amazon = 380
facebook = 350
work_week = 10 * facebook + 6 * google + 4 * amazon
print('Amount made this week')
print(work_week)

''' 7. 
A student can be enrolled to a class only if the class is 
not full and the class schedule does not conflict with her current schedule.'''
not_full = True
conflict = False
enroll = (not_full == True and conflict == False)
print('Can student enroll?')
print(enroll)

'''8. 
A product offer can be applied only if people buys more than 2 items, 
and the offer has not expired. 
Premium members do not need to buy a specific amount of products.'''
cart = ['a', 'b', 'c']
is_offer_expired = False
is_premium_member = False
is_offer_good = (len(cart) >= 2 or is_premium_member == True and is_offer_expired == False)
print('Is the offer good?')
print(is_offer_good)

''' 9.
Continue working in the data_types_and_variables.py file. 
Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions:

The password must be at least 5 characters
The username must be no more than 20 characters
The password must not be the same as the username
Bonus Neither the username or password can start or end with whitespace'''
username = 'codeup'
password = 'notastrongpassword'
is_password_long_enough = len(password) >= 5
is_password_short_enough = len(password) <= 20
is_password_not_username = password != username
does_password_have_whitespace = password == password.strip()
does_username_have_whitespace = username == username.strip()
is_valid = is_password_long_enough and is_password_short_enough and is_password_not_username \
    and does_password_have_whitespace and does_password_have_whitespace
print('Is password valid?')
print(is_valid)