"""Create a basic fuzzy logic algorithm that takes an input variable
and calculates the corresponding output using fuzzy sets and rules"""

#Import numpy and skfuzzy and assign them both shorthand aliases by writing this code:
import numpy as np
import skfuzzy as fuzz

#Accept user input
user_input = input("Enter a value between 0 and 10: ")
input_value = float(user_input)

#Assign the input variables a range of 0-10 by writing this code:
x = np.arange(0, 11, 1) #arange() creates an array (start=0, stop=11, step=1)

#Define the triangular (three sets) fuzzy sets for the input variables based on triangular membership functions
#trimf() creates the triangular membership functions
#The code determines to what degree the input belongs to each fuzzy set and uses this information to apply fuzzy rules
low = fuzz.trimf(x, [0, 0, 5]) #triangle fuzzy set for low values
medium = fuzz.trimf(x, [2, 5, 8]) #triangle fuzzy set for medium values
high = fuzz.trimf(x, [5, 10, 10]) #triangle fuzzy set for high values

#Get membership values for input_value
low_degree = fuzz.interp_membership(x, low, input_value)
medium_degree = fuzz.interp_membership(x, medium, input_value)
high_degree = fuzz.interp_membership(x, high, input_value)

#Define the fuzzy rules that determine the relationship between the input and the output
rule1 = np.fmax(low_degree, medium_degree) #if input is low or medium, then output is high
rule2 = np.fmin(medium_degree, high_degree) #if input is medium or high, then output is low

#Apply the fuzzy rules to determine the fuzzy relation between input and output
relation = np.fmax(rule1, rule2)

#Aggregate the fuzzy relation using the maximum operator
#The code combines the rules and calculates the "activated" membership function using the max and min operators
aggregated = np.fmax(low, relation)
activated = np.fmin(aggregated, medium)

#Defuzzify the relation to obtain a crisp output by writing this code
#(Centroid is a measure used in defuzzification to calculate the center or average of a fuzzy set)
output = fuzz.defuzz(x, activated, 'centroid')

#Display the crisp output by writing this code:
print("Output:", output)
