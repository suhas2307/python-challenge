import csv
import os

#Set the input file path
inputcsvpath = os.path.join("election_data.csv")
#Set the output file path
outputcsvpath = os.path.join("output.csv")

#Set variables
tot_vote_count = 0
candidate_dict = {}

#Read the file
with open(inputcsvpath,'r',newline="") as inputcsvfile:
    inputcsvreader = csv.reader(inputcsvfile,delimiter=",")
    #Read the header record
    inputcsvheader = next(inputcsvreader)
    #Read voter data
    for row in inputcsvreader:
        #increment the voter count
        tot_vote_count = tot_vote_count + 1
        #Assign csv data
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        #Update dictionary to hold the vote count for every candidate
        candidate_dict[candidate] = candidate_dict.get(candidate,0) + 1

#Create a list of tuples sorted in the descending order of the vote count. List comprehension is used
vote_candidate_list = sorted([(value,key) for (key,value) in candidate_dict.items()],reverse=True)

with open(outputcsvpath,'w') as outputfile:
    print(f"Election Results")
    outputfile.write(f"Election Results\n")
    print(f"-------------------------")
    outputfile.write(f"-------------------------\n")
    print(f"Total Votes: {tot_vote_count}")
    outputfile.write(f"Total Votes: {tot_vote_count}\n")
    print(f"-------------------------")
    outputfile.write(f"-------------------------\n")

    for vote,cdt in vote_candidate_list:
        print(f"{cdt}: {float(vote)/tot_vote_count:.3%} ({vote})")
        outputfile.write(f"{cdt}: {float(vote)/tot_vote_count:.3%} ({vote})\n")

    print(f"-------------------------")
    outputfile.write(f"-------------------------\n")
    print(f"Winner: {vote_candidate_list[0][1]}")
    outputfile.write(f"Winner: {vote_candidate_list[0][1]}\n")
    print(f"-------------------------")
    outputfile.write(f"-------------------------\n")






    