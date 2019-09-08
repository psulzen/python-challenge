# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# csvpath = os.path.join('Resources', 'Netflix.csv')
mainpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Resources', 'Polling_Results.csv')

# with open (csvpath) as csvfile:
with open(mainpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"Reading in: {csv_header}. . . please wait")

# Init some variables to zero
    rowcount = 0    # so I know how many votes there are
    candidate = []  # a list to keep the names of the candidates
    votes = []     # a list to keep all of the votes for the candidates

# Read each row of data after the header
    for row in csvreader:
        rowcount = rowcount + 1
        
        # check if this is a new candidate by looking in the list for the name
        if (row[2]) in candidate:

        # If in the votes list, increment by 1 the votes for this specific candidate
            votes[candidate.index(row[2])] += 1
        else:

        # else, add this candidate to the voter list    
            candidate.extend([row[2]])

        # add a new variable to the voter array with an initial value of 1    
            votes.extend([1])          
#            votes[candidate.index(row[2])] += 1 # adding

    print()
    print(f"Election Results")
    print(f"------------------------------------------")
    print(f"Total Votes: {rowcount}")
    winner_tot = 0 
    winner = "nobody"
    for name in candidate: 
        print(f"{name} has {votes[candidate.index(name)]} votes, for {((votes[candidate.index(name)])/rowcount*100):.3f}%")
        if votes[candidate.index(name)]>winner_tot:
            winner = name
            winner_tot = votes[candidate.index(name)]
    print(f"------------------------------------------")
    print(f"{winner} wins with {winner_tot} votes.")
    print(f"------------------------------------------")

    with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow([f"Election Results"])
        csvwriter.writerow([f"------------------------------------------"])
        csvwriter.writerow([f"Total Votes: {rowcount}"])
        winner_tot = 0 
        winner = "nobody"
        for name in candidate: 
            csvwriter.writerow([f'{name} has {votes[candidate.index(name)]} votes, for {((votes[candidate.index(name)])/rowcount*100):.3f}%'])
            if votes[candidate.index(name)]>winner_tot:
                winner = name
                winner_tot = votes[candidate.index(name)]
        csvwriter.writerow([f"------------------------------------------"])
        csvwriter.writerow([f"{winner} wins with {winner_tot} votes."])
        csvwriter.writerow([f"------------------------------------------"])

