import os, csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Pull the header row off
    csv_header = next(csvreader)

    # Store all other rows in an array of array (that are effectively tuples)
    unpacked_csv = [next(csvreader)]
    for row in csvreader:
        unpacked_csv.append(row)
    
    # Uses the length of the array to check of number of months
    number_of_votes = len(unpacked_csv)
    print(f"Total Months: {number_of_votes}")

    for row in unpacked_csv:
        
