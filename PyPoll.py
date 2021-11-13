import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#open the election results and read the file using with
#To write file and save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialize total vote counter
total_votes = 0
#Candidate Options
candidate_options = []
#to create empty candidate dictionary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winnning_count = 0 
winnning_percentage = 0

#First part to read and make lists and dict
with open(file_to_load) as election_data:
#Assign the variable to the reader function
    file_reader = csv.reader(election_data)
#print only headers
    headers = next(file_reader)
#print each row in the csv file
# to read and find 1. Total votes, 2. candidate name 3. Key value pairing for names and votes
    for row in file_reader:
        total_votes += 1 # total_votes = total_votes + 1
        #to get the candidate name from each row
        candidate_name = row[2]
        # if candidate does not match any existing candidate - Remove duplicate
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #to track candidate vote
            candidate_votes[candidate_name]=0
        #add vote to the candidte name
        candidate_votes[candidate_name]+=1
    # this needs to be modified
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")
        txt_file.write(election_results)
# end of reading first for loop for the csv file

#To find winning candidates
for candidate_name in candidate_votes:
    #retrieve vote count and percentage
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) *100
    #print each candidate and thier vote
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #determine winning vote count and candidate
    if (votes> winnning_count) and (vote_percentage > winnning_percentage):
        winnning_count = votes
        winnning_percentage = vote_percentage
        winning_candidate = candidate_name

    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)
    with open(file_to_save, "a") as txt_file:
        txt_file.write(candidate_results)



#print winning candidate results to the terminal
winning_candidate_summary =  (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winnning_count:,}\n"
    f"Winning Percentage: {winnning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#txt_file.write(winning_candidate_summary)
# Save the final vote count to the text file.
with open(file_to_save, "a") as txt_file:
    txt_file.write(winning_candidate_summary)