#Generate a Fibonacci series up to a given number 'n'.

#first method:

userInput = int(input("How many numbers should appear?"))
num1, num2 = 0, 1
count = 0
if userInput <= 0:
    print("Please enter a valid positive number!")
elif userInput == 1:
    print("The Fibonacci sequence up to ",userInput," looks like this:")
    print(num1)
else:
    print("Fibonacci sequence:")
    while count < userInput:
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1

#second method:
        
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series
n = 150
fib_series = fibonacci_series(n)
print("This is the second method: ", fib_series)