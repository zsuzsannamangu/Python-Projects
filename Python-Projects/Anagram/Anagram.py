#Check if two strings are anagrams (contain the same characters in a different order)

#First sort both strings in ascending order using the built-in sorted() method then compare them

def stringsAnagrams(stringOne, stringTwo):
    if sorted(stringOne.lower()) == sorted(stringTwo.lower()):
        return True
    else:
        return False
    
stringOne = "Light on yoga"
stringTwo = "Yoga on light"
print(stringsAnagrams(stringOne, stringTwo))