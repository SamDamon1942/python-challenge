 UC Berkeley Bootcamp
Week 3 Challenge, Part 1: PyBank

**********************************************************************************************************
In this challenge, I'm tasked with creating a Python script to analyze
the financial records of my company. I'll be given a financial dataset called "budget_data.csv"
The dataset is composed of two columns, "Date" and "Profit/Losses".

The task is to create a Python script that analyzes the records to calculate each of the 
following values:

1. The total number of months included in the dataset
2. The net total amount of "Profit/Losses" over the entire period
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
4. The greatest increase in profits (date and amount) over the entire period
5. The greates decrease in profits (date and amount) over the entire period

**********************************************************************************************************

The salient details:
1. The source dataset is called "budget_data.csv" and contains 86 records.
2. For this challenge I opted to create variables rather than lists to hold sums, counts, and dates. 
3. Overall approach:
    3.1 import a couple of python modules to faciliate file paths and manipulating the data
    3.2 create a path to the dataset
    3.3 create and initialize variables
    3.4 open the dataset with csv.reader
    3.5 read the header row and save it as an object
    3.6 loop through the dataset, and with each iteration:
        3.6.1 calculate the current profit/loss
        3.6.2 calculate the prior profit/loss
        3.6.3 calculate the monthly change
        3.6.4 determine the maximum and minimum monthly change
        3.6.5 calculate the total profit/loss
        3.6.6 calculate the total number of months
    3.7 after looping through the data:
        3.7.1 print the results to the terminal
        3.7.2 print the results to a text file called "results.csv"

 

