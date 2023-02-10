#!/usr/bin/env python
# coding: utf-8

# #### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[229]:


def is_two(thing):
    '''
    This function will check if the input is the integer 2 or the string '2'
    '''
    # check if the input is either the int 2, float 2.0 or str '2'
    if thing == 2 or thing == 2.0 or thing == '2':
        # return function as true if 2
        return True
    # for all inputs that are not 2
    else:
        # return false if not 2
        return False

# #### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[245]:


def is_vowel(letter):
    '''
    Checks if the input letter is a vowel
    '''
    # check if input is vowel and return true if vowel
    if type(letter) == str and len(letter) == 1:
        return letter.lower() in ['a', 'e', 'i', 'o', 'u']
    else: return False

# #### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.


def is_consonant(letter):
    '''
    Check if input letter is a consonant by checking if it is a vowel
    '''
    # input letter into is_vowel function
    if not is_vowel(letter) and letter.isalpha() and len(letter) == 1:
        # if letter is not a vowel, it is consonant
        return True
    # for all vowels
    else:
        # return false if letter is a vowel
        return False



# #### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.



def title_case_consonant(word):
    '''
    Function will capitalize first letter of input word if word begins with a consonant
    '''
    # check if first letter is_consonant by passing to the is_consonant function
    if is_consonant(word[0]):
        # change word to title case if first letter is consonant
        word = word.title()
        # return the capitalized word
        return word


# #### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.



def calculate_tip(tip_percent, bill_total):
    '''
    Will calculate tip amount by multiplying the bill_total by the desired tip percentage
    '''
    # return the bill total multiplied by the tip percentage
    return bill_total * tip_percent


# #### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.



def apply_discount(original_price, discount_percent=0):
    '''
    This will calculate a discounted price given an original price and a desired discount
    '''
    # returns the original price minus (the original price multiplied by discount percentage)
    return original_price - (original_price * discount_percent)


# #### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.



def handle_commas(starting_string):
    '''
    This will remove commas from an integer inputed as a string
    '''
    # replace commas in string with nothing
    num = starting_string.replace(',','')
    # convert output variable to int
    num = int(num)
    # return the output variable
    return num


# In[272]:


# #### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[107]:


def get_letter_grade(num):
    '''
    This will convert a numerical grade into a letter grade
    '''
    # check if the grade was greater than or equal to 90
    if num >= 90:
        # return letter grade as 'A'
        return 'A'
    # check if the grade was between 80 and 89
    elif num >= 80:
        # return letter grade as 'B'
        return 'B'
    # check if the grade was between 70 and 79
    elif num >= 70:
        # return letter grade as 'C'
        return 'C'
    # check if the grade was between 60 and 69
    elif num >= 60:
        # return letter grade as 'D'
        return 'D'
    # for grades below 60
    else:
        # return F as letter grade
        return 'F'


# #### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed

# In[108]:


def remove_vowels(string):
    '''
    This will check each letter in a string and return an output string with vowels removed
    '''
    # split string into letters
    string = list(string)
    # create a temp output variable
    output = ''
    # step through each letter in the string
    for letter in string:
        # check if letter is a vowel by sending to function is_vowel
        if not is_vowel(letter):
            # if letter is not a vowel, add it to the output variable
            output = output + letter
    #return the completed output variable
    return output


# #### 10.Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#  - Name will become name
#  - First Name will become first_name
#  - % Completed will become completed

# In[109]:


def normalize_name(string):
    '''
    This will convert an input string into a valid Python identifier string
    '''
    # remove leading and trailing whitespace, then convert string to lowercase
    string = string.lstrip().rstrip().lower()
    # split string into characters
    string = list(string)
    # create temp output variable
    output = ''
    # step through each character in the string
    for n in string:
        # check if the character is a space
        if n == ' ':
            # if character is space, replace with underscore
            output = output + '_'
        # check if character is a digit, and not in the first postion of output
        elif output != '' and n.isdigit():
            # add digit to output string
            output = output + n
        # check if character is valid Python identifier character
        elif str.isidentifier(n):
            # add valid character to output string
            output = output + n
    # return completed output string
    return output


# #### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[110]:


def cumulative_sum(num_list):
    '''
    This will give the cumulative sum for each number in a list of numbers
    '''
    # create temp variable to hold cumulative sum
    num = 0
    # create temp output list 
    output = []
    # step through each number in input list
    for n in num_list:
        # add input number to cumulative sum
        num = num + n
        # add cumulative sum to output list
        output.append(num)
    # return completed output list
    return output


# #### Bonus 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

# In[255]:


def twelveto24(time):
    '''
    This will take in a time in 12 hour format, then return the time in 24 hour format
    '''
    # create temp variable to store hours
    hours = ''
    # create temp variable to store minutes
    minutes = ''
    # create bool to tell if looking at hours or minutes
    is_hours = True
    # split time into list of digits
    time = list(time)
    # step through the digits of the input time
    for n in time:
        # check if the digit is the ':' character dividing hours and minutes
        if n == ':':
            # change is_hours to false
            is_hours = False
        # check if digit is either A of AM
        elif n == 'a' or n == 'A':
            #check if hours is 12AM, which converts to 00 in 24 hour format
            if hours == '12':
                # convert 12AM to 00 hour
                hours = '00'
                # return hours and minutes in 24 hour format
                return hours + ':' + minutes
                # check if hours is single digit
            elif len(hours) == 1:
                # add leading 0 to single digit hours
                hours = '0' + hours
                # return hours and minutes in 24 hour format
                return hours + ':' + minutes
            else: return hours + ':' + minutes
        # check if digit is P of PM
        elif n == 'p' or n == 'P':
            # if 12pm then add 11 to the hours
            if hours == '12':
                # return hours and minutes in 24 hour format
                return hours + ':' + minutes
            # if pm and not 12pm then add 12 to the hours
            else:
                # convert hours to int so we can add to it
                hours = int(hours) + 12
                # convert hours back into string
                hours = str(hours)
                # return hours and minutes in 24 hour format
                return hours + ':' + minutes
        # if digit is in the hour part of 12 hour time
        elif is_hours:
            # add hours digit to output hours
            hours = hours + n
        # if digit is in the minutes part of 12 hour time
        elif not is_hours:
            # add minutes value to minutes output
            minutes = minutes + n


# In[258]:

# #### Bonus write a function that does the opposite.

# In[300]:


def twentyfourto12(time):
    time = list(time)
    hours = ''
    mins = ''
    is_hours = True
    for n in time:
        if n == ':':
            is_hours = False
        elif is_hours:
            hours = hours + n
        else:
            mins = mins + n
    hours = int(hours)
    if hours == 0:
        hours = 12
        ampm = 'am'
    elif hours == 12:
        ampm = 'pm'
    elif hours > 12:
        hours = hours - 12
        ampm = 'pm'
    else:
        ampm = 'am'
        
    hours = str(hours)
    return hours + ':' + mins + ampm


# #### Bonus 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# - col_index('A') returns 1
# - col_index('B') returns 2
# - col_index('AA') returns 27

# In[219]:


def col_index(name):
    '''
    This will convert a letter column name into a number index
    It works similar to converting a binary or hexidecimal number to base-10
    The letter is converted to a base-36 number 
    then subtract 9 (to remove the 0-9 values of base 36)
    then the value is multilied by a 26 ** (position from the right) 
    '''
    # convert input name to lowercase and split it into a list
    name = list(name.lower())
    # reverse the order of the list in order to make it easier to multiply position value
    reverse_list = list(reversed(name))
    # create temp variable
    index = 0
    # loop through letters in reversed form of name, giving the letter and index in list
    for i, item in enumerate(reverse_list):
        # add to output variable 26 ** the index position * letter converted to digit
        index = index + ((26 ** i) * (int(item, 36) - 9))
    # return the temp variable
    return index