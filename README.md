# Budgeting App 

A  simple budgeting app that keeps track of user generated transactions wihtin a categorized ledger. The ledger list all the debits, deposits, withdraws, transfers to return a final net balance. The categories (objects) can be anything the user wants; food, auto, clothing, hobbies, etc. The program also creates a bar chart of all the money spent for each category in case you need a visualization. 

 Here is an example of the ledger for a category like Food: 
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

The program has 6 mains functions: 
- *Deposit function*: accepts an amount and description and returns an object which is appended to the ledger list in form of {"amount": amount, "description": description}. 
- *Withdraw function*: similar to the deposit function, but the amount passed in should be stored in the ledger as a negative number.
- *Transfer function*: accepts an amount and a destination category as arguments. The function will withdrawal the amount from the source catgeory and deposit it into the desired category
- *Check_Funds function*: accepts an amount as an argument and returns False if the amount is greater than the balance of the budget category or returns True if otherwise.
- *Get_Balance function*: returns the current balance of the budget category based on the deposits and withdrawals that have occurred. 
- *Create_Spend_Chart function*: creates a visualization of the total dollar amounts per category in the ledger. 

Here is an example of the ![Create_spend_chart bar chart](chart_visuals.png):

        
The project was originally posted [here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app) on Freecodecamp, but I modified it to handle more complexity.  
