'''
Create an Account Management program in python which handles saving (credit), withdrawal (debit) and check balance.
Before it saves an amount for a user, the user has to have an account. 
Make referals to our Order-Class application in our previous assignment. 
Here is a basic overview. 
The prograamme should be able to have three methods in a non-static class but before the credit method is called, 
it has to save a user (Just like Order/Class assignment of the place_order method)
In the get balance method, i want you to add some conditional statements to check if the transaction_type is Debit to subtract and Credit to add

***Full Requirements***
1. Create a static user class - it should have these methods below in a,b,c
a. create_user 
i. create_user method should have these parameters 
create_user({ "name": "Eugene", "age": 56, "gender": "Male", "occupation": "CEO" }) : Remember the uuid module we used to create randomized string
ii. Save it inside a users.txt file - it should be like this in the file
{ "name": "Eugene", "age": 56, "gender": "Male", "occupation": "CEO" },
The user_id would be used to identify a user we would like to tie a transaction in Account Class
NB: It should return a string (UUID) example: 32423-dsfdfdsf-324324234-dsfdsfsdfsdf (This would be used in the Account class)

b. get_user
i. get_user method should have these parameters 
get_user(user_id [uuid]) : Remember the uuid module we used to create randomized string
The user_id would be used to get a specific user information
NB: It should return a dictionary example: { "name": "Eugene", "age": 56, "gender": "Male", "occupation": "CEO" }

c. get_all_users
i. get_all_users method should have NO parameters 
get_all_users() :
NB: It should return a list with dictionaries example: 
[{ "name": "Frank", "age": 56, "gender": "Male", "occupation": "Co-founder" }, { "name": "Eugene", "age": 56, "gender": "Male", "occupation": "CEO" }, ]


2. Create a non static account class - it should have these methods below in a,b,c
a. credit 
i. credit method should have these parameters 
credit(amount [float], user_id [uuid] - A dynamic string) : Remember the uuid module we used to create randomized string
ii. Save it inside a accounts.txt file - it should be like this in the file
{ "amount": 20.00, "transaction_type": "Credit",  "user_id": "32423-dsfdfdsf-324324234-dsfdsfsdfsdf" },
The user_id would be used to identify a user we would like to tie a transaction to
NB: It should return a dictionary example: { amount_credited: 12.00, user_info: { "name": "Eugene", "age": 56, "gender": "Male", "occupation": "CEO" } }

b. debit
i. debit method should have these parameters 
debit(amount [float], user_id [uuid] - A dynamic string) : Remember the uuid module we used to create randomized string
ii. Save it inside a (the same) accounts.txt file - it should be like this in the file
{ "amount": 40.00, "transaction_type": "Debit",  "user_id": "32423-dsfdfdsf-324324234-dsfdsfsdfsdf" },
The user_id would be used to identify a user we would like to tie a transaction to.
NB: It should return a dictionary example: { amount_debited: 34.00, user_info: { "name": "Eugene", "age": 56, "gender": "Male", "occupation": "CEO" } }

c. get_balance
i. debit method should have these parameters 
get_balance(user_id [uuid] - A dynamic string) : Remember the uuid module we used to create randomized string
The user_id would be used to identify a user we would like to tie a transaction to.
NB: It should return a dictionary example: { account_balance: 50000.00, user_info: { "name": "Eugene", "age": 56, "gender": "Male", "occupation": "CEO" } }

Create simple python functions which does the following:

1. add => two parameters
2. subtract  => two parameters
3. divide => two parameters
4. multiplication => two parameters
5. get_healthy_weight => two parameters (height, weight) and returns formale => weight * (height * height)
6. get_age => two paramters => (todays_date [integers], date_of_birth [integers]) 
i. example 
get_age(20230301, 19560301) => 20230301 - 19560301

'''
