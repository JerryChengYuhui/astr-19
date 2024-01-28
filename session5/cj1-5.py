#Jerry Cheng Coding Journal 1 Session 5.

import math

def generate_sin_table(start, end, num_points):
    """Generates a table of sin(x) vs x."""
    step = (end - start) / num_points
    x_values = [start + i * step for i in range(num_points)]
    sin_values = [math.sin(x) for x in x_values]

    return zip(x_values, sin_values)

def main():
    """Main program function to output the sin(x) vs x table."""
    sin_table = generate_sin_table(0, 2, 1000)
    
    print("X Value, Sin(X)")
    for x, sin_x in sin_table:
        print(f"{x:.5f}, {sin_x:.5f}")

if __name__ == "__main__":
    main()
