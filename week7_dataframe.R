# a. Which executive received the highest salary?
# b. What is the average bonus distributed by company in financial sector?
# c. Programmatically adds a new field that denotes the average wages computed by averaging
# out individual's salary plus bonus over 12 months.
# d. Create a summary report in .txt format denoting the average wages (from c) by industry.
setwd(".....")
data <- read.csv("salariesByIndustry.csv")
df <- data.frame(data)
df$ExecutiveName[which.max(df$Salary)]
#highest_salary <- max(df$Salary) # a
result <- tapply(df$Bonus, df$CompanyType, mean)
result["Financials"] #b
df$avg_wages <- (df$Salary + df$Bonus)/12 # c
result_d <- tapply(df$avg_wages, df$CompanyType, mean)
write.csv(result_d, "dataframe_result.csv") # d, writing to csv file

# Try the same using datatable
# [i, j, by]
# SQL:  SELECT col_name WHERE col_name = "abc" GROUP BY=How to group them
# i WHERE(condition), i SELECT(viewing which col), by (GROUPBY)