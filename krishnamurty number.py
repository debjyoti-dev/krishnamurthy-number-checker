def is_krishnamurthy(n):
    def factorial(x):
        f = 1
        for i in range(1, x + 1):
            f *= i
        return f

    return n == sum(factorial(int(d)) for d in str(n))


number = int(input("Enter a number: "))
if is_krishnamurthy(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
