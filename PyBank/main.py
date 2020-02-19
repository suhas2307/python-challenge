import os
import csv

#Set the variables
tot_month = 0
tot_amt = 0
greatest_profit = 0
greatest_loss = 0
tot_change_amt = 0
prev_amt = 0

#Set the path to read the csv file
input_csv_path = os.path.join("budget_data.csv")
#Set the path for the output file
output_path = os.path.join("output.csv")

#Open the file to read data
with open(input_csv_path,'r',newline="") as input_csv_file:
    input_csv_reader = csv.reader(input_csv_file,delimiter=",")

    #Read header record
    input_csv_header = next(input_csv_reader)
    #Loop through every record in the file
    for row in input_csv_reader:
        amount = float(row[1])
        month = str(row[0])
        #Add 1 to the total number of months counter
        tot_month = tot_month + 1
        #Add the profit or loss to the accumulator
        tot_amt = tot_amt + amount
        #Calculate change in amount
        change_amt = amount - prev_amt

        #Update total change in amount from the 2nd month onwards
        if tot_month > 1:
            tot_change_amt = tot_change_amt + change_amt
        
        #Update greatest increase in profit 
        if change_amt > greatest_profit:
            greatest_profit = change_amt
            greatest_profit_month = month
        #Update greatest decrease in profit
        elif change_amt < greatest_loss:
            greatest_loss = change_amt
            greatest_loss_month = month

        #Update prev_amt to current row amt
        prev_amt = amount
    
#Calculate the average change
avg = tot_change_amt / (tot_month - 1) #No. of changes will be total months subtracted by 1
#Print analysis
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {tot_month}")
print(f"Total: {tot_amt:.0f}")
print(f"Average Change: ${avg:.2f}")
print(f"Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit:.0f})")
print(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss:.0f})")
#Write output to a file
with open(output_path,"w") as output_file:
    output_file.write(f"Financial Analysis\n")
    output_file.write(f"----------------------------\n")
    output_file.write(f"Total Months: {tot_month}\n")
    output_file.write(f"Total: {tot_amt:.0f}\n")
    output_file.write(f"Average Change: ${avg:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit:.0f})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_loss_month} (${greatest_loss:.0f})\n")


        


