setwd("C:\\Users\\yen\\Dropbox\\Codes\\2018_winter")
data <- read.csv("salariesByIndustry.csv")
library("data.table")
dt <- data.table(data)
 # find the max
max_salary_person <- dt[Salary == max(Salary),.(ExecutiveName, max(Salary))]
mean_Bonus <- dt[CompanyType=="Financials", mean(Bonus)] #
dt[, monthly:= (Salary + Bonus)/12] # c, add in new col, :=
data_to_file <- dt[, mean(monthly), by=list(CompanyType)]
data_to_file <- as.data.frame(data_to_file)

dest_file <- file("datatable_result.txt","w")
write.table(data_to_file, dest_file)
close(dest_file)

