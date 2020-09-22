# python-challenge
Two Python Challenges, PyBank and PyPoll.

### PyBank
In this part, the following tasks are done in Python and save in the "analysis.txt":

- The total number of months included in the dataset

- The net total amount of "Profit/Losses" over the entire period

- The average of the changes in "Profit/Losses" over the entire period

- The greatest increase in profits (date and amount) over the entire period

- The greatest decrease in losses (date and amount) over the entire period

**Thoughts**

The first step is to read csv file in python.

After that, we need to check if there're headers. This is important because headers should not be included in the calculation. 

Next, we are going to use the for loop to calculate the total and average values as asked in the tasks. This file has headers, so we need to 2 things: one is save the header row in a separate variable; the other is to do the calculation in the first row that contains data manually before the for loop starts. 

*This is tricky. I only managed to figure it out because my codes always read the second line of data as the first row. It happens because when calculate the changes between months, next() moves the cursor to the next line without showing it to us. 

To calculating the average, use ***total months - 1*** rather than ***total months*** because we are dealing with the changes not the monthly information per se. 

Lastly, to find the greatest increase and greatest decrease, I create a IF statement and compare the current values with the previous values that was stored in certain variables. 

### PyPoll

Your task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.
