# UC Berkeley Bootcamp
# Week 3 Challenge, Part 2: PyPoll
#
# **********************************************************************************************************
# In this challenge, I'm tasked with helping a small, rural town modernize its vote-counting process.
# I'll be given a set of poll data called "election_data.csv". The dataset is composed of three columns, 
# "Voter ID", "County", and "Candidate".
#
# The task is to create a Python script that analyzes the votes and calculates each of the following values: 
# 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
#
# **********************************************************************************************************

# Start with importing a couple of modules to help

import os               # This will allow us to create file paths across operating systems
import csv              # This allows us to manipulate comma separted values files

# create a path to the dataset
election_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0          # this is used to count the votes cast
max_votes = 0            # this is used to identify which candidate received the most votes   
winner = ""              # this identifies the winning candidate

candidate_dict={"candidate_name": "",
                "votes":0 }          #this is a dictionary called "candidate_dict" and it will be used to hold the candidate names and a count of the votes they received


# Open the CSV using the UTF-8 encoding
with open(election_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
    
    # Loop through the dataset and update the dictionary
    for row in csvreader:
        name = row[2]

        if name in candidate_dict: #checks whether the candidate name in the current row already exists in the dictionary 
            # if the candiate is already in the dictionary, add 1 to the candidate's vote count
            candidate_dict[name] = candidate_dict[name] + 1
        else:
            # if the candidate is not in the dictionary, add the candidate to the dictionary with the key "candidate_name" and update their vote count to 1
            candidate_dict[name] = 1
            #candidate_dict["votes"] = 1
        total_votes = total_votes + 1 

# becuase I created a dictionary and initialzied it with a placeholder key and corresponding placeholder value, delete that key:value pair

del candidate_dict["candidate_name"]
del candidate_dict["votes"]

# print the results to the terminal        
print("Election Results")
print()
print("----------------------------")
print()
print("Total Votes: " + str(total_votes))
print()
print("----------------------------")
print()

# Now, loop through the dictionary to get each candidate's name, their percentage of total votes cast, and the number of votes they received

for i in candidate_dict:

    candidate_votes= int(candidate_dict[i])
    candidate_pct = round(candidate_votes/total_votes * 100, 3)

    print(i + ": "+ str(candidate_pct)+ "% (" + str(candidate_votes)+")")

    if candidate_votes > max_votes:
        max_votes = candidate_votes
        winner = i
    print()

print("----------------------------")
print()
print("Winner: " + winner)
print()
print("----------------------------")

# print the results to a text file      
# specify the file to write to
output_path = os.path.join("analysis","results.txt")

#open the file using "write" mode. Specify the variable hold the contents
f = open(output_path, 'w')
f.write("Election Results\n")
f.write("\n")
f.write("----------------------------\n")
f.write("\n")
f.write("Total Votes: " + str(total_votes)+ "\n")
f.write("\n")
f.write("-----------------------------\n")
f.write("\n")

for i in candidate_dict:
    candidate_votes= int(candidate_dict[i])
    candidate_pct = round(candidate_votes/total_votes * 100, 3)
    f.write(i + ": "+ str(candidate_pct)+ "% (" + str(candidate_votes)+")" + "\n")
    f.write("\n")

    if candidate_votes > max_votes:
        max_votes = candidate_votes
        winner = i
    f.write("\n")

f.write("----------------------------\n")
f.write("\n")
f.write("Winner: " + winner + "\n") 
f.write("\n")
f.write("----------------------------")
f.close()
