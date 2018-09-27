import csv

class Industry:
    def __init__(self, name, wages, bonus):
        self.name = name
        self.wages = wages
        self.bonus = bonus
        self.count = 1

    def __str__(self):
        return "{} wages={} bonus={} count={}".format(self.name, self.wages, self.bonus, self.count)

    def adding(self, wages, bonus):
        self.wages += wages
        self.bonus += bonus
        self.count += 1

salaries = []
industries = {} # Construct dictionary for b & d, {Industries: [wages, bonus, count]}
with open("salariesByIndustry.csv", "r") as salaries_file:
    salaries_csv = list(csv.reader(salaries_file))
    salaries_csv.pop(0) # remove the first row (header)
    highest_salary = 0
    highest_salary_index = -1
    for index, each in enumerate(salaries_csv):
        # each = ['3M', 'Industrials', 'Buckley, George W.', '1720000', '2644100']
        name = each[1]
        wages = int(each[3])
        bonus = int(each[4])
        if each[1] in industries:
            # Construct subsequent record in each industry, added in new wages, bonus, and count
            industries[name].adding(wages, bonus)
        else:
            industries[name] = Industry(name, wages, bonus)# first occurrence setting
        if wages > highest_salary:
            highest_salary = wages # a. Get the highest salary and replace record
            highest_salary_index = index
        salary = [each[0], each[1], each[2], wages, bonus, (wages+bonus)/12]
        salaries.append(salary)
print("(a) The highest earner is {} making ${:,d}".format(salaries[highest_salary_index][2], highest_salary))
print("(b) The average bonus by finance sector is ${:,.2f}".format(industries["Financials"].bonus/ industries["Financials"].count))
print("(c) ", salaries)
print("(d) ", )
for key, value in industries.items():
    print("The average for {} is ${:,.2f}".format(key, value.bonus/12))
