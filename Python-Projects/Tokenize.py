# Using Python, tokenize a given paragraph into words and then into individual characters

# Given paragraph stored in the variable paragraph
paragraph = "Tokenize this paragraph into words and then into individual characters."

# Tokenize the paragraph into words using the split() method, which splits the string based on whitespace by default
words = paragraph.split()

# Print words
print("Words:", words)

# Tokenize each word into characters using a list comprehension where each character is extracted from each word in the words list
characters = [char for word in words for char in word]

# Print characters
print("Characters:", characters)