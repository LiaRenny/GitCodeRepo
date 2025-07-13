# Python
def fib_series(nn):
    series = []
    a, b = 0, 1
    for i in range(nn + 1):
        series.append(a)
        a, b = b, a + b
    return series

def fib(nn):
    if nn == 0:
        return 0
    elif nn == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, nn + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    nn = int(input("Enter the position of the Fibonacci number: "))
    series = fib_series(nn)
    print(f"Fibonacci series up to {nn}: {series}")
    print(f"The {nn}th Fibonacci number is: {fib(nn)}")