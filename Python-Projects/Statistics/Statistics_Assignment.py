#First install the necessary library (statsmodels) by executing this command from the terminal (command line):
#pip install statsmodels

#Import the required libraries:
import pandas as pd
import numpy as np
from scipy.stats import norm #normal distribution or Gaussian distribution
from scipy.stats import ttest_ind
import statsmodels.api as sm
import warnings

#Load the dataset:
dataset = pd.read_csv("/Users/Zsuzsi/Documents/GitHub/Python-Practice/AI/Statistics/dataset_1.csv")

#Perform data analysis:
num_rows, num_cols = dataset.shape
print(f"Number of rows: {num_rows}") #The count or total number of rows in a dataset.
print(f"Number of columns: {num_cols}") #The count or total number of columns in a dataset.
print("Columnns:", dataset.columns.tolist()) #Prints out all the column names

#Calculates descriptive statistics for each column in the dataset:
#Discriptive statistics provides information about the distribution (how the data is spread out), 
#the measures of central tendency (the typical or average value), and variability (how the data points differ from each other) of the data.
summary_stats = dataset.describe()
print("Descriptive statistics:")
print(summary_stats)

#Perform probability (The likelihood of an event occurring) calculation using cdf: cumulative distribution function
if len(dataset) >= 8:
    prob = norm.cdf(2.5, loc=dataset["column_1"].mean(), scale=dataset["column_1"].std()) 
    #The location (loc) keyword specifies the mean. The scale (scale) keyword specifies the standard deviation.
    print(f"Probability: {prob}")
else:
    print("Insufficient data for probability calculation")

#Perform hypothesis testing between two groups:
warnings.filterwarnings("ignore") #ignore the warning for the small sample size
group_a_data = dataset[dataset['group'] == 'A']['column_2']
group_b_data = dataset[dataset['group'] == 'B']['column_2']
if len(group_a_data) >= 8 and len(group_b_data) >= 8:
    t_stat, p_value = ttest_ind(group_a_data, group_b_data)
    #T-statistic: A measure of how statistically significant the difference between two groups is in a t-test (a statistical test to compare means of two groups).
    #P-value: The probability of obtaining the observed results (or more extreme) if the null hypothesis (assumption of no significant difference or relationship) 
      #is true (a measure of the evidence against the null hypothesis).
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
else:
    print("Insufficient data for hypothesis testing")

#Perform correlation analysis:
#Correlation Matrix: A table that shows the correlation coefficients between variables, 
   #indicating the strength and direction of the relationships (how variables are related to each other).
   #Coefficient: the estimated effect of an independent variable on the dependent variable.
numeric_columns = dataset.select_dtypes(include=[np.number]).columns
#The numpy.number class can be used as an argument to the select_dtypes method of pandas DataFrames to select or exclude the numeric columns. numpy.number represents all numeric types.
corr_matrix = dataset[numeric_columns].corr()
print("Correlation matrix:")
print(corr_matrix)

#Perform regression analysis = analyzing the relationship between variables to predict outcomes
if len(dataset) >= 8:
    X = dataset[['column_1', 'column_2', 'feature_1', 'feature_2']]
    y = dataset['target']
    X = sm.add_constant(X) #Add a column of ones to an array.
    model = sm.OLS(y, X).fit() #OLS = Ordinary Least Squares
    #Ordinary Least Squares regression, a common method used to estimate the parameters of a linear regression model 
    #by minimizing the sum of squared residuals (the measure of the difference between observed and predicted values, magnified for analysis).
    print(model.summary())
else:
    print("Insufficient data for hypothesis testing")
