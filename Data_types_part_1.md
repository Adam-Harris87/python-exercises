1.
99.9 = float
"False" = string
False = bool
'0' = string
0 = int
True = bool
'True' = string
[{}] = list
{'a' : []} = dict

2. What data type would best represent the following?
A term or phrase typed into a search box				string
Whether or not a user is logged in 						bool
A discount amount to apply to a user's shopping cart	int
Whether or not a coupon code is valid					bool
An email address typed into a registration form 		string
The price of a product									float
The email addresses collected from a registration form 	list
Information about applicants to Codeup's data science program dict

3.
Read the expression and predict the evaluated results
Execute the expression in a Python REPL.

'1' + 2
error
6 % 4
2
type(6 % 4)
int
type(type(6 % 4))
str
'3 + 4 is ' + 3 + 4
error
0 < 0
False
'False' == False
False
True == 'True'
False
5 >= -5
True
True or "42"
True
6 % 5
1
5 < 4 and 1 == 1
False
'codeup' == 'codeup' and 'codeup' == 'Codeup'
False
4 >= 0 and 1 !== '1'
True
6 % 3 == 0
True
5 % 2 != 0
True
[1] + 2
error
[1] + [2]
[1, 2]
[1] * 2
[1, 1]
[1] * [2]
error
[] + [] == []
True
{} + {}
error