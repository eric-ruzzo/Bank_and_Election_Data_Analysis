# Import os and csv libraries
import os
import csv

# Path to collect data from folder
pybankCSV = os.path.join("..", "BackupFiles", "budget_data.csv")

# Print title
print("Financial Analysis")
print("  ----------------------------")

# Create empty list to add months
months = []
profit_loss = []
difference_list = []

# Read in the CSV file
with open(pybankCSV, "r", newline="") as csvfile:

    # Split the data using commas
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        if len(profit_loss) > 1:
            difference_list.append(profit_loss[-1] - profit_loss[-2])

    # Determine total number of months and print total
    months_total = len(months)
    total_profit = sum(profit_loss)
    change = sum(difference_list)
        
    print(f"Total Months: {months_total}")
    print(f"Total Profit/Loss: ${total_profit}")
    print(f"Average Change: ${change / (months_total - 1)}")
    print(f"Greatest Increase in Profits: {months[difference_list.index(max(difference_list)) + 1]} (${max(difference_list)})")
    print(f"Greatest Decrease in Profits: {months[difference_list.index(min(difference_list)) + 1]} (${min(difference_list)})")