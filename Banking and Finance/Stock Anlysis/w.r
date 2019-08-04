library(foreign)
library(RSQLite)

con <- dbConnect(SQLite(),":memory:")

funda <- read.csv("AAPL.csv")

head(funda)

dbWriteTable(con,"funda",funda,overwrite=TRUE)


q1 <- "SELECT Open FROM funda"

result1<-dbGetQuery(con,q1)
result1

#get maximum
q5 <- "SELECT Avg(Open) FROM funda "
result5 <- dbGetQuery(con,q5)
result5


q2 <- "SELECT * FROM funda WHERE Date BETWEEN '2015-01-01' AND '2015-12-31'"
result2<-dbGetQuery(con,q2)
result2


q2 <- "SELECT * FROM funda WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND Open < 100 "
result2<-dbGetQuery(con,q2)
result2




q3 <- "SELECT * FROM funda  ORDER BY Date desc"
result3 <-dbGetQuery(con,q3)
result3

#update

q4 <- "UPDATE funda SET Open = 100 WHERE Open < 100 "
result4 <- dbExecute(con,q4)
result4







