# UC Berkeley Bootcamp
# Week 3 Challenge, Part 1: PyBank
#
# **********************************************************************************************************
# In this challenge, I'm tasked with creating a Python script to analyze
# the financial records of my company. I'll be given a financial dataset called "budget_data.csv"
# The dataset is composed of two columns, "Date" and "Profit/Losses".
#
# The task is to create a Python script that analyzes the records to calculate each of the 
# following values:
#
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greates decrease in profits (date and amount) over the entire period
#
# **********************************************************************************************************

# Start with importing a couple of modules to help

import os               # This will allow us to create file paths across operating systems
import csv              # This allows us to manipulate comma separted values files

# create a path to the dataset
budget_csv = os.path.join("Resources", "budget_data.csv")

# variables and lists will be needed to store the data

month_count = 0             # use this to count the total number of months in the dataset
total_Profit_Loss = 0       # use this to sum the profit/loss of each month
profit_loss_prior = 0       # this is the profit/loss for the prior month
profit_loss_current = 0     # this is the profit/loss for the current month
monthly_change = 0          # this is the change in profit/loss from one month to the next month
monthly_change_total = 0    # this holds the sum of the monthly changes (needed to calculate the average monthly change)
count_for_average = 0       # this holds a count of the number of monthly changes (needed to calculate the averge monthly change)
max_change = 0              # this initialize the greatest increase in monthly change in profit/loss 
max_change_date = " "       # the holds the month of the greatest increase in monthly change in profit/loss
min_change = 0              # this initialize the greatest decrease in monthly change in profit/loss
min_change_date = " "       # the holds the month of the greatest increase in monthly change in profit/loss

# Open the CSV using the UTF-8 encoding
with open(budget_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Loop through the dataset and update the variables and lists
    for row in csvreader:
        if month_count == 0: #ignore the following: monthly change (because there isn't one), average change, greatest increase, and greatest decrease 
            profit_loss_prior = int(row[1])
        else:
            profit_loss_current = int(row[1])
            monthly_change = profit_loss_current - profit_loss_prior
            #UPDATE THE COUNT
            count_for_average = count_for_average + 1
            
            #UPDATE THE TOTAL CHANGE AND CALCULATE THE AVERAGE
            monthly_change_total = monthly_change_total + monthly_change
            average_change = round(monthly_change_total/count_for_average,2)

            #UPDATE THE PRIOR PROFIT/LOSS
            profit_loss_prior = profit_loss_current
        
            if monthly_change > max_change:
                max_change = monthly_change
                max_change_date = row[0]
        
            if monthly_change < min_change:
                min_change = monthly_change
                min_change_date = row[0]

        total_Profit_Loss = total_Profit_Loss + int(row[1])
        month_count = month_count + 1

# print the results to the terminal        
print("Financial Analysis")
print()
print("----------------------------")
print()
print("Total Months: " + str(month_count))
print()
print("Total: $" + str(total_Profit_Loss))
print()
print("Averge Change: " + "($" + str(average_change)+")")
print()
print("Greatest Increase in Profits: " + max_change_date + " ($" + str(max_change) + ")")
print()
print("Greatest Decrease in Profits: " + min_change_date + " ($" + str(min_change) + ")")

# print the results to a text file      
# specify the file to write to
output_path = os.path.join("analysis","results.csv")

# open the file using "write" mode. Specify the variable hold the contents
with open(output_path, 'w') as csvfile:

    # initialize csv.write
    csvwriter = csv.writer(csvfile, delimiter=',')

    # write the first row (column headers)
    csvwriter.writerow(["Total Months", "Total Profit/Loss", "Average Change", "Date of Greatest Increase In Profits", "Greatest Increase In Profits", "Date of Greatest Decrease In Profits", "Greatest Decrease In Profits"])
    
    # write the second row (the results)
    csvwriter.writerow([month_count, total_Profit_Loss,average_change,max_change_date, max_change, min_change_date, min_change] )
    
