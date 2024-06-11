import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from scipy.stats import skew
import numpy as np

#Load the dataset
df = pd.read_csv("/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/AI-Projects/Data_Preprocessing/example_dataset.csv")

#Perform data preprocessing

#Check for missing values and fill those with zero
print(df.isnull().sum())
df.fillna(0, inplace=True)

#Remove duplicates
df.drop_duplicates(inplace=True)

#Scale numerical features using the Standardization technique
#The Standardization technique uses the statistical properties of the feature. The scaled feature will have a mean of 0 and a standard deviation of 1.
#Scaling or normalizing numerical features will ensure those are on a similar scale
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

#Check skewness of numerical columns to make them more symmetric
skewness = df_scaled.apply(lambda x: skew(x))
skew_features = skewness[abs(skewness) > 0.5].index  # Select features with skewness > 0.5
df_scaled[skew_features] = np.log1p(df_scaled[skew_features])  # Apply log transformation to skewed features

#Remove constant or near-constant features, these typically have the same value or a 
  #small number of unique values across the entire dataset. Identifying and removing these 
  #is important because they don't contribute much information to the model 
  #and can sometimes cause issues during model training.
#Calculate the percentage of unique values in each column
unique_percentages = df_scaled.nunique() / len(df_scaled)
#Define a threshold for considering a feature as near-constant (e.g., 99% of values are the same)
threshold = 0.99
#Select columns with unique percentages below the threshold
constant_features = unique_percentages[unique_percentages <= threshold].index
#Remove constant or near-constant features from the DataFrame and save the filtered dataset as df_filtered
df_filtered = df_scaled.drop(columns=constant_features)

#Create interaction terms by generating new features by multiplying two existing features together
#This will improve the predictive power of the machine learning model
df_filtered['interaction_feature'] = df_filtered['feature_1'] * df_filtered['feature_2']

#Save the preprocessed dataset
df_filtered.to_csv("/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Data_Preprocessing/preprocessed_dataset.csv", index=False)

