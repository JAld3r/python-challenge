# collect data from the csv file
import os
import csv

# file path for data
electiondata_csv = os.path.join('Pypoll', 'Resources', 'election_data.csv')

# read results in a csv file & skip the header
with open(electiondata_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

# calculate the total number of votes cast
    totalvotes = 0
    for vote in csvreader:
        if vote[0]:
            totalvotes += 1

# calculate the total number of votes each each candidate won
with open(electiondata_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    # dictionary for the votes cast per candidate
    votes_all = {}
    for vote in csvreader:
        candidate_name = vote[2]
        votes_all[candidate_name] = votes_all.get(candidate_name,0)+1

# create a text file for the results
with open('PyPoll/analysis/Election_Results.txt', 'w') as e:

    # print results for total votess
    print("Electon Results", file=e)
    print("----------------------------------------", file=e)
    print(f"Total Votes: {totalvotes}", file=e)
    print("----------------------------------------", file=e)

    # calculate the percentage of the vote for each candidate   
    for candidate_name, count in votes_all.items():
        percentile = (count / totalvotes) * 100

        # print results for each candidate
        print(f"{candidate_name}: {percentile:.3f}% ({count})", file=e)

        # determine the winner
        winner = max(votes_all, key=votes_all.get)

    # print the winner
    print("----------------------------------------", file=e)
    print(f"Winner: {winner}", file=e)
    print("----------------------------------------", file=e)