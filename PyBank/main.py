# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# input path defined and stored
mainpath = os.path.join('Resources', 'budget_Data.csv')

# output file define and stored
output_path = os.path.join('Resources', "Budget_Results.txt")

# Open the CSV file
with open(mainpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Save off the header row, just in case we want it.  Which we won't this time.   
    csv_header = next(csvreader)

    # Initilize all of the variables
    rowcount = 0     # so I know how many months there are
    run_tot = 0      # so I can get a running total of Profits and losses 
    prev_val = 0     # I need to keep track of the previous value to calculate the change      
    change = 0               # Initilize the change to a zero
    change_tot = 0         # needed to calculate average of total change 
    greatest_increase_amt = 0 # needed to calculate average of total change 
    greatest_increase_mon = 0 # needed to calculate average of total change 
    greatest_decrease_amt = 0 # needed to calculate average of total change
    greatest_decrease_mon = 0 # needed to calculate average of total change 
    
    # loop through the data
    for row in csvreader:

            # keep a running total of the row count
            rowcount += 1 

            # keep a running total of the Profits and losses 
            run_tot += int(row[1])

            # This will do calculations based on the change. The first row will not have 
            # a change yet, so only do if this is not the first row 
            if prev_val != 0:

                # Get the change by subtracting the previous value from the current
                change = int(row[1]) - prev_val

                # Keep a running total of the change 
                change_tot += change

                # Adjust the greatest increase amount as we go by saving it to a variable.
                if change > greatest_increase_amt:
                    greatest_increase_amt = change
                    greatest_increase_mon = row[0]

                # Adjust the greatest decrease amount as we go by saving it to a variable.
                if change < greatest_decrease_amt:
                    greatest_decrease_amt = change
                    greatest_decrease_mon = row[0]

            # Finally, we save the current value to "prev_val" so next loop we can determine the change
            prev_val = int(row[1])

    # We are ready to print 
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total months: {rowcount}")
    print(f"Total: {run_tot}")
    print(f"Average Change: {change_tot/(rowcount-1):.2f}")
    print(f"Greatest Increase: {greatest_increase_amt} on {greatest_increase_mon}")
    print(f"Greatest Decrease: {greatest_decrease_amt} on {greatest_decrease_mon}")

    with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
        csvwriter = csv.writer(csvfile)

    #   Print to output file  
        csvwriter.writerow([f"Financial Analysis"])
        csvwriter.writerow([f"------------------"])
        csvwriter.writerow([f"Total months: {rowcount}"])
        csvwriter.writerow([f"Total: {run_tot}"])
        csvwriter.writerow([f"Average Change: {change_tot/(rowcount-1):.2f}"])
        csvwriter.writerow([f"Greatest Increase: {greatest_increase_amt} on {greatest_increase_mon}"])
        csvwriter.writerow([f"Greatest Decrease: {greatest_decrease_amt} on {greatest_decrease_mon}"])
