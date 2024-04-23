#Implement a function to calculate the dot product of two vectors
#A dot product is a mathematical operation that takes two vectors and calculates a scalar quantity.
#Scalars have magnitude but no direction, wheras vectors have magnitude and direction
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2): #This function first checks if the vectors have the same length
        raise ValueError("Vectors must have the same length")
    dot_product_value = sum(x * y for x, y in zip(vector1, vector2)) #calculates the dot product using a generator expression and the zip function
    return dot_product_value
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result = dot_product(vector1, vector2)
print(result)  # Output: 32
