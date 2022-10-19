Budgeting APP 

A  simple budgeting app that keeps track of user generated transactions wihtin a categorized ledger. The ledger list all the debits, deposits, withdraws, transfers and finally returns the final net balance. The categories (objects) can be anything the user wants; food, auto, clothing, hobbies, etc. TThe program also creates a bar chart of all the money spent for each category in case you need a visualization. 

 Here is an example of the ledger for a category like Food: 


The program has 4 mains functions: "withdraw", "deposit", "transfer", "check funds", and "get balance".

-The deposit function accepts an amount and description and returns an object which is appended to the ledger list in form of {"amount": amount, "description": description}.
-The withdraw function is similar to the deposit function, but the amount passed in should be stored in the ledger as a negative number.
-The get_balance function returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
-The transferfunction accepts an amount and a destination category as arguments. The function will withdrawal the amount from the source catgeory and deposit it into the desired category.
-	A check_funds function accepts an amount as an argument and returns False if the amount is greater than the balance of the budget category or returns True if otherwise.

Here is an example of the Create_spend_chart bar chart:

        
The project was originally posted here on Freecodecamp, but I modified it to handle more complexity.  
