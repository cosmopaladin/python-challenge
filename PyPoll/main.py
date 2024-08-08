import os, csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Pull the header row off
    csv_header = next(csvreader)

    # Store all other rows in an array of array
    unpacked_csv = [next(csvreader)]
    for row in csvreader:
        unpacked_csv.append(row)
    
    # Uses the length of the array to check of number of votes
    number_of_votes = len(unpacked_csv)
    print(f"Total Months: {number_of_votes}")

    # Makes a set of the canadates
    canadates_bulk = [row[2] for row in unpacked_csv] 
    canadates = set(canadates_bulk)

    # Stores a tuple containing (name, % of votes, # of votes)
    # I'm not gonna lie this is fairly unreadable code, but I really wanted to use List Comprehension
    canadates_vote_totals = []
    for canadate in canadates:
        temp_total = [row[1] for row in unpacked_csv if row[2] == canadate]
        canadates_vote_totals.append((canadate, len(temp_total)/number_of_votes, len(temp_total)))
    print("--------------------")
    for canadate_tuple in canadates_vote_totals:
        print (f"{canadate_tuple[0]}: {round(canadate_tuple[1]*100, 3)}% ({canadate_tuple[2]})")
    print("--------------------")
    
    # getting the winner
    count = 0
    the_winner = "No One Voted. Democracy has died."
    for canadate in canadates_vote_totals:
        if(count < canadate[2]):
          count = canadate[2]
          the_winner = canadate[0]
    print(f"Winner: {the_winner}")

    # Write to a file
    output_file = os.path.join("output.txt")
    with open(output_file, "w", newline='') as datafile:
      datafile.write(f"Total Months: {number_of_votes}\n")
      datafile.write("--------------------\n")
      for canadate_tuple in canadates_vote_totals:
        datafile.write(f"{canadate_tuple[0]}: {round(canadate_tuple[1]*100, 3)}% ({canadate_tuple[2]})\n")
      datafile.write("--------------------\n")
      datafile.write(f"Winner: {the_winner}\n")
    
        