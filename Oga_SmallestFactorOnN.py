def smallest_factor(n):
    # Verify if the input is less than 2
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    # Identify the smallest factor, excluding 1
    for i in range(2, n + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            break


# Get user input
try:
    num = int(input("Enter an integer >= 2: "))
    smallest_factor(num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
