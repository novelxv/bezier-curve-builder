import time
import matplotlib.pyplot as plt

def bezier_curve_recursive(control_points, t):
    """ Recursively calculates the Bezier curve point at a specific t. """
    if len(control_points) == 1:
        return control_points[0]
    new_points = []
    for i in range(len(control_points) - 1):
        new_x = control_points[i][0] * (1 - t) + control_points[i + 1][0] * t
        new_y = control_points[i][1] * (1 - t) + control_points[i + 1][1] * t
        new_points.append((new_x, new_y))
    return bezier_curve_recursive(new_points, t)

def plot_bezier(control_points, num_points=1000):
    start_time = time.time()
    """ Plots the Bezier curve for a given set of control points. """
    bezier_points = [bezier_curve_recursive(control_points, t/num_points) for t in range(num_points + 1)]
    # Extract x and y coordinates from points
    x_values, y_values = zip(*bezier_points)
    control_x, control_y = zip(*control_points)
    plt.figure()
    plt.plot(x_values, y_values, 'b-', label='Bezier Curve')
    plt.plot(control_x, control_y, 'ro--', label='Control Points')
    plt.title('Bezier Curve')
    plt.legend()
    print("masuk")
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Execution time: {execution_time:.2f} ms")
    plt.show()
    print("keluar")

# Example control points and number of points to plot
control_points = [(0, 0), (3, 3), (4, 0)]
num_points = 1000

# Time and plot the curve
start_time = time.time()
plot_bezier(control_points, num_points)
# end_time = time.time()

# Print execution time
# execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
# print(f"Execution time: {execution_time:.2f} ms")