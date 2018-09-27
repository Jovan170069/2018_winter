# Title     : TODO
# Objective : TODO
# Created by: yen
# Created on: 20/9/18

# create a datable, you can construct
# using data.table(data)
# or read from file
# dt <- fread("xxx.csv")

library(data.table)

c1 <- 1:50 # create 50 numbers
# create 50 random letters of A, B, C
c2 <- sample(LETTERS[1:3], 50, replace = TRUE )
# create repeated data
c3 <- rep(c("Jurong", "Punggol", "West Coast"), 50)
dt <- data.table(c1, c2, c3) # create data table with 3 cols
View(dt) # view the data table
dt[c2 == "A"] # select rows whose c2 equals to "A"
dt[c2 == "A", mean(c1)] # compute mean of c2 whose values are "A"
dt[1:3] # select row 1 to 3
dt[,1:3] # select column 1 to 3

# task 6_1 in R
setwd(".")
dt <- fread("salariesByIndustry.csv")
