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

candidate_dict={}          #this is a dictionary called "candidate_dict" and it will be used to hold the candidate names and a count of the votes they received
candidate_name_list = []   #this is a list to hold the candidate names
candidate_pct_list= []     #this is a list to hold the percentage of total votes received
candidate_vote_list = []   #this is a list to holdthe votes received


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

for i in candidate_dict:
    candidate_votes= int(candidate_dict[i])
    candidate_pct = str(round(candidate_votes/total_votes * 100, 3))+"%"
    
    #Now, append each of the three lists
    candidate_name_list.append(i)
    candidate_pct_list.append(candidate_pct)
    candidate_vote_list.append("(" + str(candidate_votes)+")")
    
    if candidate_votes > max_votes:
        max_votes = candidate_votes
        winner = i

#Now, zip the three lists together
zipped_lists = zip(candidate_name_list, candidate_pct_list, candidate_vote_list)

# PRINT RESULTS TO THE TERMINAL        
print("Election Results")
print()
print("----------------------------")
print()
print("Total Votes: " + str(total_votes))
print()
print("----------------------------")
print()

for item1, item2, item3 in zipped_lists:
    print(item1 + ":", item2, item3)
    print()

print("----------------------------")
print()
print("Winner: " + winner)
print()
print("----------------------------")

# PRINT RESULTS TO A TEXT FILE      
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


for item1, item2, item3 in zip(candidate_name_list,candidate_pct_list,candidate_vote_list):
    concatenated_string = item1 + ": " + item2 + " " + item3
    f.write(concatenated_string)
    f.write("\n")

f.write("----------------------------\n")
f.write("\n")
f.write("Winner: " + winner + "\n") 
f.write("\n")
f.write("----------------------------")
f.close()
