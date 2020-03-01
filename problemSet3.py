#FINANCIAL PROBABILITIES:

#1. What is this data used for?

#      I think that this data is telling us data about serious deliquencies
#that someone has expenced this and the attributes that contribute to that.
#Some of these attributes include revolving utalization of unsecured lines,
#their age, the number of times (30-59 days) something has been past due, their
#debt ratios, their monthly incom, the number of open credit lines this person
#has, the number of times they have been 90 days late, the number of real
#estate loans or lines they have, thenumber of times they have been 60-89 days
#past due, and the number of dependents this person has.


#2. Create a function called loadAndCleanData that takes as an argument a
#filename and returns a Pandas dataframe. That dataframe should contain the data
#from the CSV file cleaned such that any cells missing data, containing a NaN
#value or the string "NA" are filled with 0s (this is a technique called
#zero-filling that we will talk about shortly!)

from utils import *
import pandas as pd

#data = loadAndCleanData("creditData.csv")


#3. Add a line to your Python file that uses the function to load in the
#creditData.csv file from Canvas when the Python script is run.

#   Added into the file

#4. Now that you've got your data loading, you can generate probability
#density functions for each feature. These PDFs will tell you the probability
#of a given feature occurring based on our data. You can use Kernel Density
#Estimation (KDE) to do this. Write a function called computePDF that takes as
#arguments a target feature and a dataset and generates a KDE plot for each
#feature in your data (hint: check out the plot.kde function here. You will
#need to import matplotlib.pyplot as plt and use plt.show() to make the graphs
#appear. Call that feature on each column of your dataset when you run your
#script.

#computePDF("SeriousDlqin2yrs", data)
#computePDF("Revolving", data)
#computePDF("RevolvingUtilizationOfUnsecuredLines", data)
#computePDF("age", data)
#computePDF("NumberOfTime30-59DaysPastDueNotWorse", data)
#computerPDF("DebtRatio", data)
#computePDF("MonthlyIncome", data)
#computePDF("NumberOfOpenCreditLinesAndLoans", data)
#computePDF("NumberOfTimes90DaysLate", data)
#computePDF("NumberRealEstateLoansOrLines", data)
#computePDF("NumberOfTime60-89DaysPastDueNotWorse", data)
#computePDF("NumberOfDependents", data)


#5. Given the skews that you see in your data, you might want to step back and
#take a look at what's actually in your data. You can look at the distribution
#of values in the columns. This will help you understand what data you have.
#To do this, write a function called viewDistribution that takes in the name of
#a column and a dataframe and shows a histogram of values in that column
#(hint: check out the hist function here. Comment out your computePDF function
#call and instead use viewDistribution to look at the distribution of each
#column in your dataset when the Python script is run. This should come after
#you call the loadAndCleanData function. Notice anything strange about some of
#these histograms?

#viewDistribution("SeriousDlqin2yrs", data)
#viewDistribution("Revolving", data)
#viewDistribution("RevolvingUtilizationOfUnsecuredLines", data)
#viewDistribution("age", data)
#viewDistribution("NumberOfTime30-59DaysPastDueNotWorse", data)
#viewDistribution("DebtRatio", data)
#viewDistribution("MonthlyIncome", data)
#viewDistribution("NumberOfOpenCreditLinesAndLoans", data)
#viewDistribution("NumberOfTimes90DaysLate", data)
#viewDistribution("NumberRealEstateLoansOrLines", data)
#viewDistribution("NumberOfTime60-89DaysPastDueNotWorse", data)
#viewDistribution("NumberOfDependents", data)

#   The thing that is odd is that these histograms are not
#the normal distributed historgram. It is not a nice distributions, but rather
#it is just right-sided.

#6. When your data distributions are radically skewed, you can use a log scale
#to help reveal data that is otherwise too sparse to see. Write a new version
#of the viewDistribution function called viewLogDistribution to show the log
#distribution of each column. Add this function call after your viewDistribution
#call to view the regular and log distributions of each feature.

#viewLogDistribution()

#7. Use the two distributions to identify three bins per column that divide your
#data into roughly equal numbers. What are those bins? Note you do not need bins
#for "SeriousDlqin2yrs" as that is the feature you are modeling (it is your
#dependent variable).

#   The three bins that would devide our data into roughly equal numbers are
#"NumberOfTime30-59DaysPastDueNotWorse", "NumberOfTimes90DaysLate", and
#"NumberOfTime60-89DaysPastDueNotWorse."

#8. Write a function called computeDefaultRisk that takes four arguments---a
#column name, a bin (as an array [start,end]), a target feature, and a
#dataframe---and returns the probability that someone will be at least 90 days
#delinquent on their account (in other words, "SeriousDlqin2yrs" = 1). Keep in
#mind that this probability is conditional, that means you'll want to use the
#equation for conditional probabilities to compute it. In plain English, you
#should compute the probability that a loan will become seriously delinquent
#given your target feature falls into the bin range. For example, if I'm
#looking at ages between 0 and 40, I want to compute the probability that a
#loan will go into serious delinquency given the applicant is between 0 and 40.

#computeDefaultRisk("SeriousDlqin2yrs", 0, 40, data)

#9. Print out the risk of default for each of the feature bins in your dataset.
#Note it's helpful to label these with the feature and bins such that you can
#better understand your output.

#    Done!

#RATING SCHEMES:

#10. In your main file, use your loadAndCleanData function to load in
#newLoans.csv.

data = loadAndCleanData("newLoans.csv")

#11. Use your conditional probabilities to predict the probability of default
#for each row in your CSV file. To do this, write a function called
#predictDefaultRisk that takes a row from your dataset as a parameter and
#returns the risk of default based on that data and the probabilities you
#computed from creditData.csv (hint: you might want to have predictDefaultRisk
#take a second parameter representing the risk of default for various data
#features computed from creditData.csv). You will want to compute the risk of
#default using a weighted sum with the following weights:



#12. Store the result of this function in the SeriousDlqin2yrs column.

#    Done

#13. Plot the distribution of risks using your computePDF function. What do
#you notice about this distribution?

#computePDF("SeriousDlqin2yrs", data)
#computePDF("Revolving", data)
#computePDF("RevolvingUtilizationOfUnsecuredLines", data)
#computePDF("age", data)
#computePDF("NumberOfTime30-59DaysPastDueNotWorse", data)
#computerPDF("DebtRatio", data)
#computePDF("MonthlyIncome", data)
#computePDF("NumberOfOpenCreditLinesAndLoans", data)
#computePDF("NumberOfTimes90DaysLate", data)
#computePDF("NumberRealEstateLoansOrLines", data)
#computePDF("NumberOfTime60-89DaysPastDueNotWorse", data)
#computePDF("NumberOfDependents", data)
