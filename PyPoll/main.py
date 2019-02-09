# Import os and csv libraries
import os
import csv

# Path to collect data from folder
pypollCSV = os.path.join("..", "PyPoll", "election_data.csv")

# Print title
print("Election Results")
print("-------------------------")

# Create empty lists for candidate votes and counts of votes
votes = []
vote_counts = []

# Read in the CSV file
with open(pypollCSV, "r", newline="") as csvfile:

    # Split the data using commas
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    # Loop through rows to add to list of candidate votes
    for row in csvreader:
        votes.append(row[2])

# Use len function to find total votes for all candidates and set as a variable
total_votes = len(votes)

# Cast votes list as a set and sort it to get alphabetical list of candidates and set as a variable
candidates = sorted(set(votes))

# Print total number of votes
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through candidates list and add up matching names in votes list
# Append count of votes for each candidate into vote counts list
for name in candidates:
    vote_counts.append(votes.count(name))

# Zip the lists into a dictionary with vote count as key and candidate as value
candidate_totals = dict(zip(vote_counts, candidates))

# Loop through dictionary to find largest key and print to document
for x in range(len(candidate_totals)):

    # Find largest number of votes and set as a variable
    most_votes = max(candidate_totals)

    # Find name associated with largest number of votes
    most_votes_name = candidate_totals.get(most_votes)

    print(f"{most_votes_name}: {round((most_votes / total_votes) * 100, 3)}% ({most_votes})")
    
    # Remove largest key so that the next largest is the max for the following loop
    candidate_totals.pop(most_votes)

# Zip lists again to refill empty dictionary after loop
candidate_totals = dict(zip(vote_counts, candidates))
print("-------------------------")

# Reset variable for most votes and most votes name
most_votes = max(candidate_totals)
most_votes_name = candidate_totals.get(most_votes)

# Use .get dictionary function to get value of largest index
print(f"Winner: {most_votes_name}")
print("-------------------------")

output = open("Pypoll.txt", "w")
print("Election Results", file=output)
print("-------------------------", file=output)
print(f"Total Votes: {total_votes}", file=output)
print("-------------------------", file=output)
for x in range(len(candidate_totals)):
    most_votes = max(candidate_totals)
    most_votes_name = candidate_totals.get(most_votes)
    print(f"{most_votes_name}: {round((most_votes / total_votes) * 100, 3)}% ({most_votes})", file=output)
    candidate_totals.pop(most_votes)
candidate_totals = dict(zip(vote_counts, candidates))
most_votes = max(candidate_totals)
most_votes_name = candidate_totals.get(most_votes)
print("-------------------------", file=output)
print(f"Winner: {candidate_totals.get(max(candidate_totals))}", file=output)
print("-------------------------", file=output) 