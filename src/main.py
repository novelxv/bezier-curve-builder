import brute_force as brute
import divide_and_conquer as dac

def read_input_from_txt(file_path):
    """
    Reads the input from a txt file and returns the values
    """
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        iterations = int(file.readline().strip())
        algorithm = int(file.readline().strip())
        control_points = []
        for _ in range(n):
            x, y = map(float, file.readline().strip().split())
            control_points.append((x, y))
    
    return n, iterations, algorithm, control_points

def display_welcome_message():
    print("================================================")
    print("  Welcome to the Bézier Curve Animator ✨✨✨ ")
    print("================================================")
    print("\nThis program allows you to animate the formation of Bézier curves using either the Brute Force or Divide and Conquer method.")
    print("\nPlease follow the prompts to input your control points and select the desired algorithm for the animation.")
    print("\nLet's get started!\n")

def main():
    display_welcome_message()
    # Select the input method
    print("Select the input method:")
    print("1. Manual input")
    print("2. Read from a file")
    input_method = int(input("Enter the number of the input method: "))
    if input_method == 1:
        # Take input from the user for the control points
        control_points = []
        n = int(input("\nEnter the number of control points: "))
        if n < 2:
            print("At least 2 control points are required to form a Bezier curve.")
            return
        for i in range(n):
            x, y = map(float, input(f"Enter the x and y coordinates of point {i + 1}: ").split())
            control_points.append((x, y))
        # Take input from the user for the number of iterations
        iterations = int(input("Enter the number of iterations: "))
        if iterations < 0:
            print("At least 0 iteration is required.")
            return
        # Input selection for the algorithm to use
        print("\nSelect the algorithm to use:")
        print("1. Brute Force")
        print("2. Divide and Conquer")
        algorithm = int(input("Enter the number of the algorithm: "))
    elif input_method == 2:
        file_path = input("\nEnter the file path: ")
        file_path = "../test/" + file_path
        n, iterations, algorithm, control_points = read_input_from_txt(file_path)
    else:
        print("Invalid input. Please enter 1 or 2.")
        return
    
    if algorithm == 1:
        brute.plot_bezier_brute_force(control_points, iterations)
    elif algorithm == 2:
        print("\nDo you want to animate the curve? (y/n)")
        animate = input().lower()
        if animate == 'y':
            dac.plot_bezier_divide_and_conquer_animate(control_points, iterations)
        else:
            dac.plot_bezier_divide_and_conquer(control_points, iterations)
    else:
        print("Invalid input. Please enter 1 or 2.")
        return
    
    print("\nGoodbye! Hope you enjoyed the bezier curve 💞")
    
if __name__ == "__main__":
    main()