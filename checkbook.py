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
# - current running total balance
# - each transaction will have:
#  - transaction type
#  - transaction amount
#  - ** transaction id
#  - ** transaction description
#  - ** transaction timestamp
#  - ** transaction category

# In[1]:


def menu():
    print('What would you like to do?')
    print()
    print('1: View current balance')
    print('2: Add a debit (withdrawal)')
    print('3: Add a credit (deposit)')
#     print('*** 4: View previous transactions')
#     print('*** 5: View transactions by category')
#     print('*** 6: View transactions by date')
#     print('*** 7: Search transactions by description')
#     print('*** 8: Modify previous transaction')
    print('4: Exit')
    print()
    while True:
        choice = input('Please enter your selection: ')
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice < 5:
                return choice
        else:
            print('Invalid selection')


# In[2]:


import os
import csv


# In[3]:


tran_cols = ['type','amount']
# tran_cols = ['type', 'amount', 'category', 'description', 'date', 'time', 'id']


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


# In[6]:


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
    print(f'Current balance is: ${total}')
    if total < 0:
        print('WARNING: ACCOUNT IS OVERDRAWN')


# In[7]:


def get_transaction_details(trans_type):
    #ask for amount
    #repeat if invalid input
    while True:
        amount = input('Please enter amount: ')
        if amount.isdigit():
            amount = float(amount)
            if amount > 0.00:
                break
            else:
                print('Amount cannot be negative')
        else:
            print('Invalid input')
    
    #** ask for category
    
    #** ask for description
    
    #** get current time and date
    
    #** create id number
    
    details = {'type':trans_type, 'amount':amount}
#     details = {'type':trans_type, 'amount':amount, 'cat':cat, 'desc':desc, 'date':date,
#               'time':time, 'id':id}
    add_to_ckbk(details)
    return amount


# In[8]:


def add_debit():
    print('Debit (withdrawal):')
    amount = get_transaction_details('withdrawal')    
    print(f'Withdrawl of {amount} added to checkbook.')
    view_current_balance()


# In[9]:


def add_credit():
    print('Credit (deposit):')
    amount = get_transaction_details('deposit')   
    print(f'Deposit of {amount} added to checkbook.')
    view_current_balance()


# In[10]:


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
        print('Goodbye')
        exit()
        break
    # elif choice == 4:
    #     view_prev_trans()
    # elif choice == 5:
    #     view_trans_by_cat()
    # elif choice == 6:
    #     view_trans_by_date()
    # elif choice == 7:
    #     search_trans_by_desc()
    # elif choice == 8:
    #     modify_prev_trans()
    elif choice == 9:
        print('Goodbye')
        exit()
        break
        

