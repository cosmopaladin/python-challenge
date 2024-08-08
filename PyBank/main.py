# I'm adding this as an extra commit because it's funny
# So I didn't know about the list comprehension shortcut for unpacking CSVs. 
# Then I read the code in the class I missed after finishing this part lmao
import os, csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Pull the header row off
    csv_header = next(csvreader)

    # Store all other rows in an array of array (that are effectively tuples)
    unpacked_csv = [next(csvreader)]
    for row in csvreader:
        unpacked_csv.append(row)
    
    # Uses the length of the array to check of number of months
    number_of_months = len(unpacked_csv)

    # Total Profit
    # Also creates an array containing only the number
    sum = 0
    just_the_numbers = []
    for row in unpacked_csv:
        just_the_numbers.append(row[1])
        sum += int(row[1])

    # Uses array of numbers to compute avg change
    previous = 0
    changes = []
    for row in just_the_numbers:
        if (previous == 0):
          previous = row
        else:
          changes.append(int(row) - int(previous))
          previous = row

    total = 0
    for row in changes:
      total += row
    avg = total/len(changes)        

    # Neat example of the Stride feature of ranges in python I'm keeping here for future reference
    # for row in zip(unpacked_csv[0::2], unpacked_csv[1::2]):
    #   print(f"{row}")
  
    # max and min
    max = max(changes)
    min = min(changes)
    
    # Print to terminal
    print(f"Total Months: {number_of_months}")
    print(f"Total: ${sum}")
    print(f"Average Change: $ {avg}")
    print(f"Greatest Increase in Profits {max}")
    print(f"Greatest Decrease in Profits {min}")
   
    # Write to a file
    output_file = os.path.join("output.txt")

    with open(output_file, "w", newline='') as datafile:
      datafile.write(f"Total Months: {number_of_months}\n")
      datafile.write(f"Total: ${sum}\n")
      datafile.write(f"Average Change: $ {avg}\n")
      datafile.write(f"Greatest Increase in Profits {max}\n")
      datafile.write(f"Greatest Decrease in Profits {min}\n")

