#import csv
import csv
#import os
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#open the election results and read the file using with
#To write file and save the file to a path
file_to_write = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    print(election_data)
#Assign the variable to the reader function
    file_reader = csv.reader(election_data)
#print each row in the csv file
    #for row in file_reader:
        #print(row)
#print only headers
    headers = next(file_reader)
    print(headers)