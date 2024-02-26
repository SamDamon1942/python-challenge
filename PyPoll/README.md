 UC Berkeley Bootcamp
Week 3 Challenge, Part 2: PyPoll

**********************************************************************************************************
In this challenge, I'm tasked with helping a small, rural town modernize its vote-counting process.
I'll be given a set of poll data called "election_data.csv"
The dataset is composed of thre columns, "Voter ID", "County, and "Candidate".

The task is to create a Python script that analyzes the votes and calculates each of the 
following values:

1. The total number of votes cast
2. A comlete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote

**********************************************************************************************************

The salient details:
1. The source dataset is called "election_data.csv" and contains 369,711 records.
2. For this challenge I opted to create a dictionary to hold the voting results. I also used variables for calculation percentages and to identify the winner. 
3. Overall approach:
    3.1 import a couple of python modules to faciliate file paths and manipulating the data
    3.2 create a path to the dataset
    3.3 create and initialize variables and a dictionary object
    3.4 open the dataset with csv.reader
    3.5 read the header row and save it as an object
    3.6 loop through the dataset, and with each iteration:
        3.6.1 determine if the candidate's name is in the dictionary and if so, increment that candidate's vote count.
              If the candidate's name isn't in the dictionary, add that name and set the vote count to 1.
    3.7 after looping through the data:
        3.7.1 delete the place holder key:value in the dictionary
        3.7.2 print the total votes
        3.7.3 calculate each candidate's percentage of the overall votes cast
        3.7.4 print the results to the terminal
        3.7.5 print the results to a .txt file

 

