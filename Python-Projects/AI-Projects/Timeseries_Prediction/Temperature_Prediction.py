"""Time series prediction assignment: predict and visualize daily temperatures

Time seres prediction involves forecasting future values based on historical data 
patterns by identifying trends, reoccurance, regularity, and other patterns.
"""

#Install necessary libraries: pip install pandas Prophet matplotlib plotly
#Prophet is a forecasting tool from the Prophet library in Python used for generating forecasts based on historical data patterns

#Import required libraries
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics import mean_absolute_error

#Load dataset (df represents a DataFrame object)
df = pd.read_csv(r"/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/AI-Projects/Timeseries_Prediction/daily_temperature.csv")

#Convert the Date column to datatime and sort the data
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True) #sort the dataframe by the values in the Date column in asc order, modifying the original DataFrame (inplace=True)
#When inplace=True is used, the sorting operation is applied directly to the DataFrame df without creating a new sorted DataFrame

#Prepare the dataset for Prophet
df_prophet = df.rename(columns={'Date': 'ds', 'Temperature': 'y'})

#Select the New York data only
df_prophet = df_prophet[df_prophet['City'] == 'New York']

#Initilize and fit the model
model = Prophet(daily_seasonality=True) #This creates a Prophet model object with daily seasonality enabled
#Seasonality refers to recurring patterns or cycles in the data that occur at regular intervals (e.g., daily, weekly, yearly)
model.fit(df_prophet) #The fit() method is used to train the model on the provided data (fit = train)

#Make a dataframe called future for predictions that contains the dates for which you want to make predictions
future = model.make_future_dataframe(periods=0) #periods=0 indicates that you want predictions for the same dates as your original data,
                                                # without adding any additional future periods beyond what's already in your data.
forecast = model.predict(future) #The forecast df will contain the predicted values

#Merge the forecast with the original data
df_prophet.set_index('ds', inplace=True) #This line sets the index of the df_prophet df to the column 'ds'
forecast.set_index('ds', inplace=True)
df_merged = df_prophet.join(forecast[['yhat', 'yhat_lower', 'yhat_upper']], how='inner') #The how='inner' argument specifies that only rows with matching dates
                                                                                        #from both DataFrames should be included in the merged DataFrame: df_merged.
                                                                                        #yhat_lower and yhat_upper: lower and upper bounds of the predictions
#Reset the index for plotting purposes
df_merged.reset_index(inplace=True) #After this operation, the index of df_merged will be reset to the default integer index, 
                            #and the original index (which was set to dates in the previous steps) will become a regular column in the DataFrame.

#Calculate the Mean Absolute Error (MAE) between actual (y_test) and predicted (predictions) values using sklearn
y_test = df_merged['y'].values #This line extracts the actual temperature values from the DataFrame df_merged and stores them in the NumPy array y_test.
predictions = df_merged['yhat'].values #This line extracts the predicted temperature values from the DataFrame df_merged and stores them in the NumPy array predictions.
mae = mean_absolute_error(y_test, predictions) #MAE is a common metric used to evaluate the accuracy of a regression model by measuring the average absolute difference between the actual and predicted values.
print(f"Mean Absolute Error: {mae}")

#Plot the actual vs predicted temperatures:
plt.figure(figsize=(10, 6)) #the figure will be 10 inches wide and 6 inches tall
plt.plot(df_merged['ds'], df_merged['y'], 'b-', label='Actual Temperature', marker='o', markersize=8) 
#df_merged['y'] is used as the y-axis values
#df_merged['ds'] is used as the x-axis values
#'b-' specifies that the line color is blue ('b') and the line style is solid ('-')
#marker='o' specifies that circular markers should be used at each data point.
plt.plot(df_merged['ds'], df_merged['yhat'], 'r-', label='Predicted Temperature', marker='o', markersize=8)

for i, txt in enumerate(df_merged['y']): #This loop iterates through the values in the 'y' column of the df_merged DataFrame, 
                                         #where enumerate() provides both the index (i) and the value (txt) from the column.
    plt.annotate(round(txt, 2), (df_merged['ds'][i], df_merged['y'][i]), textcoords="offset points", xytext=(0,10), ha='center')
    #Add an annotation to the plot for each data point
    #round(txt, 2) rounds the value (txt) to 2 decimal places for display in the annotation
    #ha='center' specifies horizontal alignment of the annotation text to be centered around the specified coordinates.
for i, txt in enumerate(df_merged['yhat']):
    plt.annotate(round(txt, 2), (df_merged['ds'][i], df_merged['yhat'][i]), textcoords="offset points", xytext=(0,10), ha='center') 

#Run the functions
plt.legend() #a legend serves as a visual aid that enhances the readability and interpretability of your plots
plt.xlabel('Date') #plt.xlabel('Date'): Sets the label for the x-axis as 'Date'.
plt.ylabel('Temperature')
plt.title('Actual vs. Predicted Temperatures')
plt.xticks(rotation=45) #Rotates the x-axis tick labels by 45 degrees for better readability if the dates are overlapping.
plt.tight_layout() #Adjusts the spacing between subplots to make sure everything fits nicely in the figure.
plt.show() #Displays the plot