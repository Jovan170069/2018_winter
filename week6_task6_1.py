"""
You need the file salariesByIndustry.csv for this workshop.
Import the csv file into python program and store data in appropriate data types. Write suitable python codes to answer the followings:
a. Which executive received the highest salary?
b. What is the average bonus distributed by company in financial sector?
c. Programmatically adds a new field that denotes the average wages computed by averaging out individual’s salary plus bonus over 12 months.
d. Create a summary report in .txt format denoting the average wages (from c) by industry.
"""
import csv

output_file = open("task6_1_summary.txt","w")
salaries = []

count = 0
industries = {} # Construct dictionary for b & d, {Industries: [wages, bonus, count]}
with open("salariesByIndustry.csv", "r") as salaries_file:
    salaries_csv = list(csv.reader(salaries_file))
    salaries_csv.pop(0) # remove the first row (header)
    highest_salary = 0
    highest_salary_index = -1
    for index, each in enumerate(salaries_csv):
        # each = ['3M', 'Industrials', 'Buckley, George W.', '1720000', '2644100']
        wages = int(each[3])
        bonus = int(each[4])
        if each[1] in industries:
            # Construct subsequent record in each industry, added in new wages, bonus, and count
            industries[each[1]] = [industries[each[1]][0] + wages, industries[each[1]][1] + bonus, industries[each[1]][2]+1]
        else:
            industries[each[1]] = [wages, bonus, 1] # first occurrence setting
        if wages > highest_salary:
            highest_salary = wages # a. Get the highest salary and replace record
            highest_salary_index = index
        salary = [each[0], each[1], each[2], wages, bonus, (wages+bonus)/12]
        salaries.append(salary)
print("(a) The highest earner is {} making ${:,d}".format(salaries[highest_salary_index][2], highest_salary), file=output_file)
print("(b) The average bonus by finance sector is ${:,.2f}".format(industries["Financials"][1]/ industries["Financials"][2]), file=output_file)
print("(c) ", salaries, file=output_file)
print("(d) ", file=output_file)
for key, value in industries.items():
    print("The average for {} is ${:,.2f}".format(key, value[1]/value[2]), file=output_file)
output_file.close()

