import brute_force as brute
import divide_and_conquer as dac

def main():
    # Take input from the user for the control points
    control_points = []
    n = int(input("Enter the number of control points: "))
    if n < 2:
        print("At least 2 control points are required to form a Bezier curve.")
        return
    for i in range(n):
        x, y = map(float, input(f"Enter the x and y coordinates of point {i + 1}: ").split())
        control_points.append((x, y))
    # Input selection for the algorithm to use
    print("\nSelect the algorithm to use:")
    print("1. Brute Force")
    print("2. Divide and Conquer")
    algorithm = int(input("Enter the number of the algorithm: "))
    
    if algorithm == 1:
        brute.plot_bezier_brute_force(control_points, num_points=1000)
    elif algorithm == 2:
        iterations = int(input("\nEnter the number of iterations: "))
        if iterations < 0:
            print("At least 0 iteration is required.")
            return
        all_points = [control_points]
        dac.plot_bezier_divide_and_conquer(control_points, all_points, iterations)
    else:
        print("Invalid input. Please enter 1 or 2.")
        return
    
    print("\nGoodbye! Hope you enjoyed the bezier curve 💞")
    
if __name__ == "__main__":
    main()