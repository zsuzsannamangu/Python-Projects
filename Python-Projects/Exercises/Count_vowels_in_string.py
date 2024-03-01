#Count the number of vowels in a given string

sentence = "Write a Python program to count the number of vowels in a given string"

#initializing count variable
count = 0

#creating an array of vowels
vowels = ["a", "e", "i", "o", "u"]

#len(x) gives the length of a string
for i in range(len(sentence)):
    if sentence[i] in vowels:
        count += 1

print("Number of vowels: ", count)