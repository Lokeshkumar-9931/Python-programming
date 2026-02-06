#factorial
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return  n*fact(n-1)
print(fact(5))    

def fibonacci_series(n):
    # First two terms of the Fibonacci series
    a, b = 0, 1
    count = 0
    print("Fibonacci series:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b  # Update terms
        count += 1
# Input from the user
terms = int(input("Enter the number of terms: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_series(terms)
