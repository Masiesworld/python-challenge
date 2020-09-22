import csv
import os


# Read in the files
csvpath = os.path.join("/Users/meixi/Desktop/bootcamp/Homework/HW3/python-challenge/PyBank", "Resources", "budget_data.csv")
out_bank_path = os.path.join("/Users/meixi/Desktop/bootcamp/Homework/HW3/python-challenge/PyBank","analysis","Bank_analysis.txt")

# create the output variables
counts_of_months = 0
net_total = 0
net_change = 0
max_net_increase = [0]
max_increase_month = [""]
max_net_decrease = [0]
max_decrease_month = [""]
lst = []

with open(csvpath) as file:
    budget_data = csv.reader(file, delimiter = ",")

    # IF there are headers
    if csv.Sniffer().has_header:
        next(budget_data)
        row1 = next(budget_data)
        counts_of_months += 1

        float_net_total = float(row1[1])
        net_total += float_net_total
        start_net = float(row1[1])

    for row in budget_data:  
        # counts rows and total net
        counts_of_months += 1
        float_net_total = float(row[1])
        net_total += float_net_total

        net_change = float_net_total - start_net
        start_net = float(row[1])
        
        if net_change >= max_net_increase[0]:
            max_net_increase[0] = net_change
            max_increase_month = row[0]
        if net_change <= max_net_decrease[0]:
            max_net_decrease[0] = net_change
            max_decrease_month = row[0]


with open(out_bank_path, 'w') as bank_file:


    print("Financial Analysis", file=bank_file)
    print("-----------------------------------------", file=bank_file)
    print("Total Months: {}".format(counts_of_months), file=bank_file)
    print(f"Total: ${net_total}", file=bank_file)
    print(f"Average Change: ${round(net_change/85,2)}", file=bank_file)
    print(f"Greatest Increase in Profits: {max_increase_month} (${max_net_increase[0]})", file=bank_file)
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_net_decrease[0]})", file=bank_file)


bank_file.close()



