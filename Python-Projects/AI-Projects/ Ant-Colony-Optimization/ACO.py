"""This code implements an Ant Colony Optimization (ACO) algorithm for solving a problem. 
The algorithm starts by initializing a population of ants, each of which constructs a “tour” 
by iteratively selecting the next city based on a combination of pheromone information. 
Pheromone levels are updated based on the quality of the constructed tours, and the best tour is kept 
track of during the iterations. The algorithm iterates for a specified number of iterations, and 
at the end, the best tour and its corresponding distance are returned. This ACO algorithm utilizes 
pheromone evaporation, local pheromone update, and global pheromone update to guide the ants towards 
finding an optimal or near-optimal solution.
"""

#Import numpy and it a shorthand aliases
import numpy as np

#Define the distance matrix
distance_matrix = np.array([
    [0, 3, 1, 3, 5],
    [4, 0, 9, 7, 6],
    [8, 5, 0, 1, 5],
    [3, 7, 1, 6, 2],
    [5, 3, 3, 1, 0],
])

#Define the number of cities
num_cities = distance_matrix.shape[0]
#The shape attribute returns the dimensions of the array. If distance_matrix has a rows and b columns,
#distance_matrix.shape = (a,b), so distance_matrix.shape[0] is a, so the rows, which is 5 in this case

#Define the number of ants
num_ants = 20

#Initialize the pheromone level matrix (a matrix that represents the amount of pheromone on each path)
def ant_colony_optimization(num_iterations):

    #initialize pheromone level matrix
    pheromone_level = np.ones((num_cities,num_cities))
    #ones() function allows you to create an array of a given shape and type, filled with ones, 
      #it creates a unit matrix to perform matrix operations
      #ones(3) - creates a one-dimensional array. ones(2, 3) - creates a multidim. array, 2 rows, 3 columns:
      #[[1, 1, 1] 
      # [1, 1, 1]]
    
    #initialize the heuristic information matrix 
    #(a matrix providing guidance for path selection based on problem-specific knowledge)
    heuristic_info = 1 / (distance_matrix + np.finfo(float).eps) #avoid division by zero
    """np.finfo(datatype) = give me the smallest possible positive number that the float dtype can represent
    on my machine:
    np.finfo() gets the machine epsilon for a given float type
    epsilon denotes an arbitrarily small positive number
    """

    #define alpha and beta parameters 
    #(parameters that determine the relative importance of pheromone and heuristic information 
    #in ant decision-making during optimization)
    alpha = 1.0
    beta = 2.0

    #initialize the best path and distance, and the ant paths and distances
    best_distance = float('inf') #float('inf') represents positive infinity in Python
    best_path = []
    best_iteration = -1 #this variable will keep track of the iteration with the best distance

    for iteration in range(num_iterations):
        #initialize ant paths and distances
        ant_paths = np.zeros((num_ants, num_cities), dtype=int)
        ant_distances = np.zeros(num_ants)

        #choose the starting city randomly and construct the path
        for ant in range(num_ants):
            #choose starting city randomly
            current_city = np.random.randint(num_cities)
            visited = [current_city]

            #construct the path
            for _ in range(num_cities - 1):
                #calculate the selection probabilities
                selection_probs = (pheromone_level[current_city] ** alpha) * (heuristic_info[current_city] ** beta)
                selection_probs[np.array(visited)] = 0 #set selection probabilities of visited cities to 0

                #choose the next city based on the selection probabilities
                next_city = np.random.choice(np.arange(num_cities), p=(selection_probs / np.sum(selection_probs)))
                #np.random.choice(a, size=None, replace=True, p=None) = p: 1-D array-like: the probabilities associated with each entry in a.

                #update the path and visited list
                ant_paths[ant, _+1] = next_city #_+1 is like i+1
                visited.append(next_city)

                #update the distance
                ant_distances[ant] += distance_matrix[current_city, next_city]

                #update the current city
                current_city = next_city

            #update the distance to return to the starting city
            ant_distances[ant] += distance_matrix[current_city, ant_paths[ant, 0]]

        #update the pheromone level based on the ant paths
        pheromone_level *= 0.5 #evaporation
        for ant in range(num_ants):
            for city in range(num_cities - 1):
                pheromone_level[ant_paths[ant, city], ant_paths[ant, city+1]] += 1 / ant_distances[ant]
            pheromone_level[ant_paths[ant, -1], ant_paths[ant, 0]] += 1 / ant_distances[ant]

        #update the best path and distance if a better solution is found
        min_distance_idx = np.argmin(ant_distances) 
        #The numpy.argmin() method returns indices of the min element of the array in a particular axis
        if ant_distances[min_distance_idx] < best_distance:
            best_distance = ant_distances[min_distance_idx]
            best_path = ant_paths[min_distance_idx]
            best_iteration = iteration #update the best_iteration variable

    return best_path, best_distance, best_iteration

#Run the Ant Colony Optimization algorithm
num_iterations = 250 #number of iterations
best_path, best_distance, best_iteration = ant_colony_optimization(num_iterations)

#Display the best path and distance
print("Here is the best path: ", best_path)
print("Here is the best distance: ", best_distance)
print("Iteration with the best distance: ", best_iteration)