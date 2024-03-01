#1.
#Find the largest element in a list

myList = [27, 4, 30, 29, 11, 69]
myList.sort()

#printing the last element:
print(myList[-1])

#or:
print(max(myList))




#2.
#Check if a given string is a pangram (contains all letters of the alphabet)

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string = "the quick brown fox jumps over the lazy dog"
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

#or
#Using Python Set: Convert the given string into set and then check if the alphabet set is greater than or equal
    #to it or not. If the string set is greater or equal print yes otherwise no

#Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are 
    #List, Tuple, and Dictionary, all with different qualities and usage. A set is a collection which is 
    #unordered, unchangeable*, and unindexed.

"""Python ascii() is a built-in function that escapes all the non-ASCII 
characters in the string and returns a printable representation of an object be it string, 
tuple, list, dictionary, etc.

The string ascii_lowercase will give the lowercase letters 'abcdefghijklmnopqrstuvwxyz'."""

from string import ascii_lowercase
def ispangram2(string):
    alphabet = set(ascii_lowercase)
    return set(string.lower()) >= alphabet
print(ispangram2("the quick brown fox jumps over the lazy dog"))




#3.
#Reverse the words in a given sentence

string = "the quick brown fox jumps over the lazy dog"

#reversing words in a given string:
s = string.split()[::-1]
#creating empty list:
createdList = []
for i in s:
    #appeanding reversed words to createdList
    createdList.append(i)
#Join the list in the reverse order which ultimately is the reversed sentence.
print(" ".join(createdList))

#or
def reverse_sentence(sentence):
    words = sentence.split()
    reverse_sentence = " ".join(reversed(words))
    return reverse_sentence
print(reverse_sentence("Hello World"))





#4.
#Find the first non-repeated character in a given string

def FirstCharacter(s):
    for i in s:
        if (s.find(i, (s.find(i)+1))) == -1:
            print ("The first non-repeated character is: ",i)
            break
    return
s = "python program to find the first non-repeated character in a given string"
FirstCharacter(s)




#5.
#Sort a list of strings based on their lengths, from shortest to longest.
"""sorted() is a built-in function with the key parameter
sorted syntax = sorted(iterable, key, reverse)
Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.
Key(optional): A function that would serve as a key or a basis of sort comparison, ex: key=len
Reverse(optional): If True, then the iterable would be sorted in reverse (descending) order, by default it is set as False."""

def sorting(listOfAnimals):
    newListOfAnimals = sorted(listOfAnimals, key=len)
    return newListOfAnimals
listOfAnimals = ["zebra", "fastantelope", "lion", "bigelephant", "giraffe", "hippo"]
print(sorting(listOfAnimals))




#6.
#Find the second smallest element in a list.

numberList = [2, 56, 34, 123, 202, 402, 12, 43]
def find_secondsmallest(numberList):
    numberList.sort()
    print("Second smallest element is: ",numberList[1])
    #print("Second largest element is: ",numberList[length-2])
find_secondsmallest(numberList)

