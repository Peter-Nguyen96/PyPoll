import csv
import os

#Declare Variables
number_votes = 0
candidate_options =[]
candidate_votes = {}
total_votes = 0
percentage = 0
# Whatever, funny string for winner variable.  If this name comes up there is a problem with code.
winner = "Donald J. Biden"

# Loading data and output path
load_file = os.path.join('Resources', 'election_results.csv')
save_file = os.path.join("Analysis", "elections_analysis.txt")

with open(load_file) as dataset:
    # Python reader to use csv data in python
    file_reader = csv.reader(dataset)
    # Ignore header
    headers = next(file_reader)

    # Counts the total number of votes for each candidate by checking if...
    for row in file_reader:
        number_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options: # ... the candidate is in the dictionary
            # add candidate to dict, and since current row counts as candidate vote, == 1
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 1
            # Always keep adding up total votes
            total_votes = total_votes + 1
        else:
            # adds vote to candidate in dictionary
            candidate_votes[candidate_name] += 1
            total_votes = total_votes + 1 

#Printing and writing data to text file



with open(save_file,"w") as data_output:
    # Just summary formatting
    data_output.write("Election Results\n")
    data_output.write("--------------------\n")
    data_output.write(f'Total Votes: {number_votes}\n')
    data_output.write("--------------------\n")

    # Loop to calculate percentage
    for candidate_index in candidate_votes:
        votes = candidate_votes[candidate_index]
        percentage = (votes/total_votes) * 100
        #Output Candidate Name: Percentage of votes (total votes from candidate votes)
        # could have just consolidated all into candidate votes dict instead of candidate names, thats a useless list.
        data_output.write(f'{candidate_index}: {percentage:.1f}% ({candidate_votes[candidate_index]:,})\n')
    
    data_output.write("--------------------\n")
    # Loop to calculate winner
    # Write data to txt and print in terminal
    total_votes = 0 
    for index in candidate_votes:
        if candidate_votes[index] > total_votes:
            total_votes = candidate_votes[index]
            winner = index
    data_output.write(f'The election winner is: {winner}')
    print(f'The winner is: {winner}')