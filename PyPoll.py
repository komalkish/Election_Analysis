#import csv
import csv
#import os
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#open the election results and read the file using with
#To write file and save the file to a path
file_to_write = os.path.join("analysis", "election_analysis.txt")
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
with open(file_to_load) as election_data:
    print(election_data)
#Assign the variable to the reader function
    file_reader = csv.reader(election_data)
#print only headers
    headers = next(file_reader)
     #print(headers)
#print each row in the csv file
    #total_votes = 0
    for row in file_reader:
        total_votes += 1
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
for candidate_name in candidate_votes:
    #retrieve vote count and percentage
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) *100
    #determine winning vote count and candidate
    if (votes> winnning_count) and (vote_percentage > winnning_percentage):
        winnning_count = votes
        winnning_percentage = vote_percentage
        winning_candidate = candidate_name
#print winning candidate results to the terminal
winning_candidate_summary =  (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winnning_count:,}\n"
    f"Winning Percentage: {winnning_percentage:.1f}%\n"
    f"-------------------------\n")
#print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
print(winning_candidate_summary)
    #candidate_votes[candidate_name] +=1
#with open(file_to_save, "w") as txt_file: