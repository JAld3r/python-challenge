# Dependencies
import os
import csv

# input file path
budgetdata_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# define variables
total_months = 0
total_PL = 0
changes = []

# increase & decrease variables
g_increase = ["", 0]
g_decrease = ["", 0]

# reader for csv file
with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)

    # start loop through all data
    for row in csvreader:
        
        # total months tracker
        total_months += 1
        # total P&L tracker
        total_PL += int(row[1])
        # P&L change tracker
        if total_months > 1:
            current_month_PL = int(row[1])
            previous_PL = int(previous_row[1])
            change_PL = current_month_PL - previous_PL
            changes.append(change_PL)  
            
            # greatest increase & decrease tracker
            if change_PL > g_increase[1]:
                g_increase[0] = row[0]
                g_increase[1] = change_PL
            if change_PL < g_decrease[1]:
                g_decrease[0] = row[0]
                g_decrease[1] = change_PL

        previous_row = row
# average change calculation   
change_average = sum(changes) / len(changes)

# print results to the text file
with open('PyBank/analysis/Budget_Results.txt', 'w') as b:
    print("Financial Analysis", file=b)
    print("----------------------", file=b)
    print(f"Total Months: {total_months}", file=b)
    print(f"Total ${total_PL}", file=b)
    print(f"Average Change: ${change_average:.2f}", file=b)
    print(f"Greatest Increase in Profits: {g_increase[0]} (${g_increase[1]})", file=b)
    print(f"Greatest Decrease in Profits: {g_decrease[0]} (${g_decrease[1]})", file=b)