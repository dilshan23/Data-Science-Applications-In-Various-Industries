#The binary classification goal is to predict if the client will subscribe a bank term deposit


"""Input variables:
   # bank client data:
   1 - age (numeric)
   2 - job : type of job (categorical: "admin.","blue-collar","entrepreneur","housemaid","management","retired","self-employed","services","student","technician","unemployed","unknown")
   3 - marital : marital status (categorical: "divorced","married","single","unknown"; note: "divorced" means divorced or widowed)
   4 - education (categorical: "basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown")
   5 - default: has credit in default? (categorical: "no","yes","unknown")
   6 - housing: has housing loan? (categorical: "no","yes","unknown")
   7 - loan: has personal loan? (categorical: "no","yes","unknown")
   # related with the last contact of the current campaign:
   8 - contact: contact communication type (categorical: "cellular","telephone") 
   9 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
  10 - day_of_week: last contact day of the week (categorical: "mon","tue","wed","thu","fri")
  11 - duration: last contact duration, in seconds (numeric). Important note:  this attribute highly affects the output target (e.g., if duration=0 then y="no"). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
   # other attributes:
  12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
  13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
  14 - previous: number of contacts performed before this campaign and for this client (numeric)
  15 - poutcome: outcome of the previous marketing campaign (categorical: "failure","nonexistent","success")
   # social and economic context attributes
  16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)
  17 - cons.price.idx: consumer price index - monthly indicator (numeric)     
  18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)     
  19 - euribor3m: euribor 3 month rate - daily indicator (numeric)
  20 - nr.employed: number of employees - quarterly indicator (numeric)

  Output variable (desired target):
  21 - y - has the client subscribed a term deposit? (binary: "yes","no")
"""

import pandas as pd 
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("bank-additional-full.csv",sep = ';')
print df.head()

df.data = df.iloc[:,[0,19]] # or  df.iloc[:,[2,3,6]]  --> select only 2,3 and 6th columns  | df.iloc[:,0:19] --> all columns from 1st to 20th columns
df.target = df['y']
print df.target.head()


Xtrain, Xtest, ytrain, ytest = train_test_split(df.data, df.target,random_state=42,test_size = 0.20)


print Xtrain
print ytrain

#model = GaussianNB()
model = LogisticRegression()
model
model.fit(Xtrain, ytrain)

print model.score(Xtrain, ytrain)

#output = 0.88 = 88% accuracy




###new model
#one hot encoding
df.data1 = df.iloc[:,0:19] #new training data set with all varikables where cat. variables are onehotencoded
df.data1 = pd.get_dummies(df.data1)


for c in df.data1.columns:
  print c


df.target1 = df['y']
print df.target1.head()


Xtrain1, Xtest1, ytrain1, ytest1 = train_test_split(df.data1, df.target1,random_state=42,test_size = 0.20)


model1 = LogisticRegression()
model1
model1.fit(Xtrain1, ytrain1)

print model1.score(Xtrain1, ytrain1)

#output 0.9103793626707132
