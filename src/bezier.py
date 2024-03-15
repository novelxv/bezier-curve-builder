import matplotlib.pyplot as plt
import time

def midpoint(point1, point2):
    """ 
    Mengembalikan titik tengah antara dua titik 
    """
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

def insert_midpoints(arr, midpoints):
    for i in range(len(arr) - 1, 0, -1):
        arr.insert(i, midpoints[i - 1])
    return arr

def bezier(control_points, curve_points, iterations):
    if iterations == 0:
        return control_points, curve_points
    else:
        new_control_points = []
        new_points = [control_points[0]]
        for i in range(1, len(control_points)):
            mid = midpoint(control_points[i-1], control_points[i])
            new_points.append(mid)
            new_control_points.append(mid)
        new_points.append(control_points[-1])

        curve_points.append(new_points[0])
        midpoints = []
        for i in range(1, len(new_control_points)):
            mid = midpoint(new_control_points[i-1], new_control_points[i])
            curve_points.append(mid)
            midpoints.append(mid)
        curve_points.append(new_points[-1])
        new_control_points = insert_midpoints(new_control_points, midpoints)
        new_control_points.insert(0, control_points[0])
        new_control_points.append(new_points[-1])

        return bezier(new_control_points, curve_points, iterations-1)


# def midpoint_bezier(control_points, iteration):
#     """ 
#     Constructs Bezier curve points using the midpoint algorithm for the given iteration.
#     """
#     if iteration == 0:
#         return control_points
#     else:
#         new_points = [control_points[0]]
#         for i in range(1, len(control_points)):
#             mid = (
#                 (control_points[i-1][0] + control_points[i][0]) / 2,
#                 (control_points[i-1][1] + control_points[i][1]) / 2
#             )
#             new_points.append(mid)
#         new_points.append(control_points[-1])

#         return midpoint_bezier(new_points[:len(new_points)//2], iteration-1) + \
#                midpoint_bezier(new_points[len(new_points)//2-1:], iteration-1)[1:]

def plot_midpoint_bezier(control_points, curve_points, iteration):
    start_time = time.time()
    """ Plots the Bezier curve using the midpoint algorithm for a given set of control points and iterations. """
    bezier_points = bezier(control_points, curve_points, iteration)[1]
    control_points = bezier(control_points, curve_points, iteration)[0] + control_points
    # Extract x and y coordinates from points
    x_values, y_values = zip(*bezier_points)
    control_x, control_y = zip(*control_points)
    
    plt.figure()
    plt.plot(x_values, y_values, 'b-', label='Bezier Curve')
    plt.plot(control_x, control_y, 'ro--', label='Control Points', color='red', markersize=0.5)
    plt.title(f'Bezier Curve with {iteration} iterations')
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Execution time: {execution_time:.2f} ms")
    plt.legend()
    
    plt.show()

def main():
    control_points = []
    curve_points = []
    n = int(input("Enter the number of control points: "))
    for i in range(n):
        x, y = map(float, input(f"Enter the x and y coordinates of point {i + 1}: ").split())
        control_points.append((x, y))
    iterations = int(input("Enter the number of iterations: "))


    plot_midpoint_bezier(control_points, curve_points, iterations)

if __name__ == "__main__":
    main()