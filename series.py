

def fibonacci(n):
    if n <= 0:
        return "please enter a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else: return fibonacci(n-1 + fibonacci(n-2)

n = int(input("Enter the number of terms: "))

for i in range(1, n+1):
    print(fibonacci(i))


def lucas(n):
    if n <= 0:
        return 'Please enter a positive integer'
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else: return lucas(n-1) + lucas(n-2)


def sum_series(n, n0=0, n1=1):
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n-1, n1, n0+n1)
