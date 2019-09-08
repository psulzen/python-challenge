# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# input path defined and stored
mainpath = os.path.join('Resources', 'budget_Data.csv')

# output file define and stored
output_path = os.path.join('Resources', "new.txt")

# Open the CSV file
with open(mainpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Save off the header row, just in case we want it.  Which we won't this time.   
    csv_header = next(csvreader)

    # Read each row of data after the header
    rowcount = 0     # so I know how many months there are
    run_tot = 0      # so I can get a running total of Profits and losses 
    prev_val = 0     # I need to keep track of the previous value to calculate the change     
   # firstrowf = True # I need to exclud the first row when I calc the change since there is no prior row
    
    change = 0               # Initilize the change to a zero
    change_tot = 0         # needed to calculate average of total change 
    greatest_increase_amt = 0 # needed to calculate average of total change 
    greatest_increase_mon = 0 # needed to calculate average of total change 
    greatest_decrease_amt = 0 # needed to calculate average of total change
    greatest_decrease_mon = 0 # needed to calculate average of total change 
    
    for row in csvreader:
            rowcount += 1 
            #run_tot = run_tot + int(row[1])
            run_tot += int(row[1])
            if prev_val != 0:
                change = int(row[1]) - prev_val
                change_tot = change_tot + change
                if change > greatest_increase_amt:
                    greatest_increase_amt = change
                    greatest_increase_mon = row[0]
                if change < greatest_decrease_amt:
                    greatest_decrease_amt = change
                    greatest_decrease_mon = row[0]


            prev_val = int(row[1])
            #firstrowf = False


            #x == x + 1 ' == would check if they are equal 
            #print("total number of months is " row[0])
    #print (row[0])
    #print (row[1])
    #print(len(row))
    print(f"Financial Analysis")
    print(f"------------------")
    print(f"Total months: {rowcount}")
    print(f"Total: {run_tot}")
#    print(f"Average Change: {run_tot/rowcount}")
#    print(f"Last Change: {change}")
    print(f"Last Change: {change_tot}")
    print(f"Average Change: {change_tot/(rowcount-1)}")
    print(f"Greatest Increase: {greatest_increase_amt} on {greatest_increase_mon}")
    print(f"Greatest Decrease: {greatest_decrease_amt} on {greatest_decrease_mon}")

    with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
        csvwriter = csv.writer(csvfile)
        #, delimiter='')

        csvwriter.writerow([f"Financial Analysis"])
        csvwriter.writerow([f"------------------"])
        csvwriter.writerow([f"Total months: {rowcount}"])
        csvwriter.writerow([f"Total: {run_tot}"])
        csvwriter.writerow([f"Average Change: {change_tot/(rowcount-1)}"])
        csvwriter.writerow([f"Greatest Increase: {greatest_increase_amt} on {greatest_increase_mon}"])
        csvwriter.writerow([f"Greatest Decrease: {greatest_decrease_amt} on {greatest_decrease_mon}"])
