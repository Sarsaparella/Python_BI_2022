# Homework 7 - Functional programming

Requirments: **Python 3.7** (script was written in Google Colab)

This folder contains [functional.py](http://functional.py) script inside of which you can find four functions:

🍓 sequential_map - takes any amount of functions as an arguments first and container with values. The function returns modified container after sequential application of functions on recieved container

🐌 consensus_filter - takes any amount of logical functions and container with values and returns only those values from container that were true to the conditions in all functions. 

🐣 conditional_reduce - takes only two functions and one container with values. First function must be logical and values that are true to it’s condition are transferred to the second function that reduces them to only one number

🍄 func_chain - receives any amount of functions and transfers those functions into another function. It returns the result of the sequential application of those functions.

Example:

my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4))

my_chain(37)

Answer: (9.75, 9)