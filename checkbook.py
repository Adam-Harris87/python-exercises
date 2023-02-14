#!/usr/bin/env python
# coding: utf-8

# ## checkbook application
# Build a .py file that will be run from the command line.
# 
# When run, the application should welcome the user, and prompt them for an action to take:
# 
# - view current balance
# - add a debit (withdrawal)
# - add a credit (deposit)
# - exit
# - The application should notify the user if the input is invalid and prompt for another choice.
# - The application should persist between times that it is run.
# 
# Example, if you run the application, add some credits, exit the application and run it again, you should still see the balance that you previously created. In order to do this, your application will need to store its data in a text file. Consider creating a file where each line in the file represents a single transaction.
# Utilize functions to call the balance, debit, credit, and exit

# ## Bonus
# - Add a menu item that allows the user to view all historical transactions
# - Assign categories to each transaction
#  - Add a menu item to allow the user to view all the transactions in a given category
#  - Provide the user with summary statistics about the transactions in each category
# - Keep track of the date and time that each transaction happened
#  - Allow the user to view all the transactions for a given day
#  - Hint: Make sure your list of previous transactions includes the timestamp for each
# - Allow the user to optionally provide a description for each transaction
# - Allow the user to search for keywords in the transaction descriptions, and show all the transactions that match the user's search term
# - Allow the user to modify past transactions

# application will:
# have a while loop to:
# - display menu options
# - continue asking for input until proper input is recieved
# - reject wrong inputs
# we will check existance of a balance file for the user, 
# 
# if one does not exists, we will create balance file, or we will open the balance file
# 
# view current balance will print out the current balance from file
# 
# add debit will subtract amount from balance and save debit into file
# 
# add credit will addd amount to balance and save info to file
# 
# balance file will save:
# - each transaction will have:
#  - transaction type
#  - transaction amount
#  - ** transaction id
#  - ** transaction description
#  - ** transaction timestamp
#  - ** transaction category

# In[1]:


import os
import csv
from datetime import datetime


# In[2]:


def menu():
    print('What would you like to do?')
    print()
    print('1: View current balance')
    print('2: Add a debit (withdrawal)')
    print('3: Add a credit (deposit)')
    print('4: View previous transactions')
#     print('*** 5: View transactions by category')
#     print('*** 6: View transactions by date')
#     print('*** 7: Search transactions by description')
#     print('*** 8: Modify previous transaction')
    print('5: Exit')
    print()
    while True:
        choice = input('Please enter your selection: ')
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice < 6:
                return choice
        else:
            print('Invalid selection')


# In[3]:


tran_cols = ['type', 'amount', 'category', 'description', 'date', 'time']


# In[4]:


def check_for_balance_file():
    if not os.path.exists('checkbook_balance.csv'):
        # if transaction checkbook file does not exist, create one
        print('Checkbook file does not exist')
        print('Creating new checkbook')
        with open('checkbook_balance.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=tran_cols)
            writer.writeheader()


# In[5]:


def add_to_ckbk(details):
    with open('checkbook_balance.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=tran_cols)
        writer.writerow(details)


# In[20]:


def view_current_balance():
    total = 0
    with open('checkbook_balance.csv', 'r') as f:
        ckbk_content = csv.DictReader(f, fieldnames=tran_cols)
        transactions = [line for line in ckbk_content][0:]
    for tran in transactions:
        if len(transactions) == 1:
            break
        elif tran['type'] == 'deposit':
            total += float(tran['amount'])
        elif tran['type'] == 'withdrawal':
            total -= float(tran['amount'])
    total = round(total, 2)
    print(f'Current balance is: ${total:,}')
    if total < 0:
        print('WARNING: ACCOUNT IS OVERDRAWN')


# In[7]:


def get_deposit_cat():
    # display list of deposit category types
    print()
    print('Choose deposit type from selection:')
    print('1: Checking account')
    print('2: Savings account')
    print('3: Certificate of deposit')
    print('4: Money market account')
    #ask user to choose a deposit category number
    while True:
        print()
        cat_type = input('Enter category number: ')
        #check for valid int input
        if cat_type.isdigit():
            cat_type = int(cat_type)
            if 0 < cat_type < 5:
                #return category type
                if   cat_type == 1: return 'Checking'
                elif cat_type == 2: return 'Savings'
                elif cat_type == 3: return 'CD'
                elif cat_type == 4: return 'Money_Market'
            else:
                print('Invalid input')
        else:
            print('Invalid input')
    #return category type


# In[8]:


def get_withdrawal_cat():
    # display list of withdrawl category types
    print()
    print('Choose withdrawal category type from selection:')
    print('1: Food')
    print('2: Transportation')
    print('3: Housing')
    print('4: Utilities')
    print('5: Entertainment')
    print('6: Bills')
    print('7: Other')
    #ask user to choose a withdrawl category number
    while True:
        print()
        cat_type = input('Enter category number: ')
        #check for valid int input
        if cat_type.isdigit():
            cat_type = int(cat_type)
            if 0 < cat_type < 8:
                #return category type
                if   cat_type == 1: return 'Food'
                elif cat_type == 2: return 'Transportation'
                elif cat_type == 3: return 'Housing'
                elif cat_type == 4: return 'Utilities'
                elif cat_type == 5: return 'Entertainment'
                elif cat_type == 6: return 'Bills'
                elif cat_type == 7: return 'Other'
            else:
                print('Invalid input')
        else:
            print('Invalid input')


# In[9]:


def get_transaction_details(trans_type):
    #ask for amount
    #repeat if invalid input
    while True:
        amount = input('Please enter amount: ')
        try:
            amount = float(amount)
            amount = round(amount, 2)
            if amount > 0.00:
                break
            else:
                print('Amount cannot be negative')
        except ValueError:
            print('Invalid input')
    
    #** ask for category
    if trans_type == 'deposit':
        cat = get_deposit_cat()
    elif trans_type == 'withdrawal':
        cat = get_withdrawal_cat()
    
    #** ask for description
    #ask user to enter description
    desc = input('Please enter transaction description (optional): ')
    
    #** get current time and date
    now = datetime.now()
    date = now.strftime("%Y/%m/%d")
    time = now.strftime("%H:%M:%S")
    
    #** create id number
    #look at checkbook max id number
    #id = current_max + 1
    
    details = {'type':trans_type, 'amount':amount, 'category':cat,
               'description':desc, 'date':date, 'time':time}
    add_to_ckbk(details)
    return amount


# In[10]:


def add_debit():
    print()
    print('Debit (withdrawal):')
    amount = get_transaction_details('withdrawal')
    print()
    print(f'Withdrawl of {amount} added to checkbook.')
    view_current_balance()


# In[11]:


def add_credit():
    print()
    print('Credit (deposit):')
    amount = get_transaction_details('deposit')
    print()
    print(f'Deposit of {amount} added to checkbook.')
    view_current_balance()


# In[38]:


def view_prev_trans():
    with open('checkbook_balance.csv', 'r') as f:
        ckbk_content = csv.DictReader(f, fieldnames=tran_cols)
        transactions = [line for line in ckbk_content][1:]
    print('|   type    |    amount   |     category   |    date    |   time   |                 description              |')
    print('---------------------------------------------------------------------------------------------------------------')
    for tran in transactions:
        tran_type = tran['type']
        tran_amount = tran['amount']
        tran_cat = tran['category']
        tran_date = tran['date']
        tran_time = tran['time']
        tran_desc = tran['description'][:40]
        print(f' {tran_type:<10} | ${tran_amount:>11}| {tran_cat:>14} | {tran_date:>1} | {tran_time:>7} | {tran_desc:>40} |')


# In[14]:


def view_trans_by_cat():
    with open('checkbook_balance.csv', 'r') as f:
        ckbk_content = csv.DictReader(f, fieldnames=tran_cols)
        transactions = [line for line in ckbk_content][1:]
    # get a sum of transaction amounts per category 
    #blah
    # cycle through each tran creating a list per category???
    # function to get sum per category???
        


# In[15]:


def view_trans_by_date():
    with open('checkbook_balance.csv', 'r') as f:
        ckbk_content = csv.DictReader(f, fieldnames=tran_cols)
        transactions = [line for line in ckbk_content][1:]
    # ask user for date to display
    # display transactions on given date


# In[27]:


print('Welcome to your checkbook!')
check_for_balance_file()
while True:
    print()
    choice = menu()
    #1: View current balance
    #2: Add a debit (withdrawal)
    #3: Add a credit (deposit)
    #*** 4: View previous transactions
    #*** 5: View transactions by category
    #*** 6: View transactions by date
    #*** 7: Search transactions by description
    #*** 8: Modify previous transaction
    #9: Exit
    if choice == 1:
        view_current_balance()
    elif choice == 2:
        add_debit()
    elif choice == 3:
        add_credit()
    elif choice == 4:
        view_prev_trans()
    # elif choice == 5:
    #     view_trans_by_cat()
    # elif choice == 6:
    #     view_trans_by_date()
    # elif choice == 7:
    #     search_trans_by_desc()
    # elif choice == 8:
    #     modify_prev_trans()
    elif choice == 5:
        print('Goodbye')
        exit()
        break
        

