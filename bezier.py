import matplotlib.pyplot as plt
import time

def midpoint_bezier(control_points, iteration):
    """ 
    Constructs Bezier curve points using the midpoint algorithm for the given iteration.
    """
    if iteration == 0:
        return control_points
    else:
        new_points = [control_points[0]]
        for i in range(1, len(control_points)):
            mid = (
                (control_points[i-1][0] + control_points[i][0]) / 2,
                (control_points[i-1][1] + control_points[i][1]) / 2
            )
            new_points.append(mid)
        new_points.append(control_points[-1])

        return midpoint_bezier(new_points[:len(new_points)//2], iteration-1) + \
               midpoint_bezier(new_points[len(new_points)//2-1:], iteration-1)[1:]

def plot_midpoint_bezier(control_points, iteration):
    """ Plots the Bezier curve using the midpoint algorithm for a given set of control points and iterations. """
    bezier_points = midpoint_bezier(control_points, iteration)
    # Extract x and y coordinates from points
    x_values, y_values = zip(*bezier_points)
    control_x, control_y = zip(*control_points)
    plt.figure()
    plt.plot(x_values, y_values, 'b-', label='Bezier Curve')
    plt.plot(control_x, control_y, 'ro--', label='Control Points')
    plt.title(f'Bezier Curve with {iteration} iterations')
    plt.legend()
    plt.show()

def main():
    control_points = []
    n = int(input("Enter the number of control points: "))
    for i in range(n):
        x, y = map(float, input(f"Enter the x and y coordinates of point {i + 1}: ").split())
        control_points.append((x, y))
    iterations = int(input("Enter the number of iterations: "))

    start_time = time.time()
    plot_midpoint_bezier(control_points, iterations)
    end_time = time.time()

    # Print execution time
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Execution time: {execution_time:.2f} ms")

if __name__ == "__main__":
    main()