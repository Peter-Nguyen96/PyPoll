# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes_dict = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
with open(file_to_load) as county_data:
    county_reader = csv.reader(county_data)
    header = next(county_reader)

    for row in county_reader:
        county = row[1]
        if county not in county_list:
            county_list.append(county)
            county_votes_dict[county] = 1
            total_votes += 1
        else:
            county_votes_dict[county] += 1
            total_votes += 1

    print(county_votes_dict)
    print(total_votes)


        
    

               




    