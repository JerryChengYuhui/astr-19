#Jerry Cheng Coding Journal 1 Session3

def f(x):
    # Function to calculate x**3 + 8
    return x**3 + 8

# Main function of the program
def main():
    # Calling the function f with x = 9
    result = f(9)
    print("The result is:", result)

    # If statement to check if result is larger than 27
    if result > 27:
        print("YAY!")

# Call the main function
if __name__ == "__main__":
    main()
