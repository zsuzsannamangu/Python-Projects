"""Import the "random" module (which provides various functions and methods to generate random numbers, 
   select random elements, shuffle sequences, and more) by writing this code:"""

import random

#Assign all constants, the target phrase to be matched, the number of individuals 
   #in the population and the probability of mutation, by writing this code:

#Constants:
TARGET_PHRASE = "I love programming with Python!" #the target phrase to be matched
POPULATION_SIZE = 250 #Number of individuals in the population
MUTATION_RATE = 0.02 #Probability of mutation

#Generate the initial population by writing this code:

def generate_population():
        population = []
        for _ in range(POPULATION_SIZE): #for _ in range(number) indicates that the loop var is irrelevant, _ stands for i
            #the range function creates a seq of numbers which the "for" loop then iterates over
            individual = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!') for _ in range(len(TARGET_PHRASE)))
            #join will join the words with a '' space in front of them
            #random.choice chooses a random element from a list
            population.append(individual)
        return population

#Calculate the fitness score by writing this code:

def calculate_fitness(individual):
    score = 0
    for i in range(len(TARGET_PHRASE)):
        if individual[i] == TARGET_PHRASE[i]:
            score += 1
    return score

#Select the parents based on their fitness by writing this code:

def select_parents(population):
    parents = []
    for _ in range(2):
        parents.append(max(population, key=calculate_fitness)) #max() returns item with highest value
    return parents
    
#Create the offspring through crossover by writing this code:

def crossover(parents):
    offspring = ""
    crossover_point = random.randint(0, len(TARGET_PHRASE) - 1)
    for i in range(len(TARGET_PHRASE)):
        if i <= crossover_point:
            offspring += parents[0][i]
        else:
            offspring += parents[1][i]
    return offspring

#Mutate the offspring by writing this code:

def mutate(offspring):
    mutated_offspring = ""
    for i in range(len(offspring)):
        if random.random() < MUTATION_RATE: #the random.random() method returns a random floating no. btw 0 and 1
            mutated_offspring += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!')
        else:
            mutated_offspring += offspring[i]
    return mutated_offspring

#Create the main portion of the genetic algorithm by writing this code:

def genetic_algorithm():
    population = generate_population()
    generation = 1

    while True:
        print(f"Generation {generation} - Best Fit: {max(population, key=calculate_fitness)}")

        if TARGET_PHRASE in population:
            break

        new_population = []
        for _ in range(POPULATION_SIZE // 2): #// is floor division: rounds the division down to the nearest whole number
            parents = select_parents(population)
            offspring = crossover(parents)
            mutated_offspring = mutate(offspring)
            new_population.extend([offspring, mutated_offspring])
            #extend() list function: to add elements of an iterable(ex: string, list...) to the end of another list
        
        population = new_population
        generation += 1

        #f-strings are formatted string literals, offers a way for string interpolation: the insertion of sg 
        #of a different nature into something else. used with {}

#Run the genetic algorithm
genetic_algorithm()

"""
1. this code initializes a population of random strings
2. evaluates their fitness scores
3. selects the fittest individuals as parents
4. performs crossover and
5. performs mutation to generage new offspring
6. iterates through generations until the target phrase is found of a satisfactory solution is achieved
7. the progress is printed after each generation to track the best fitness score
"""