import matplotlib.pyplot as plt
import time

def midpoint(point1, point2):
    """ 
    Mengembalikan titik tengah antara dua titik 
    """
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

# def bezier(points, iterations):
#     """
#     Membagi titik kontrol menjadi dua bagian dan menghitung titik tengah
#     Hingga jumlah iterasi yang diberikan tercapai
#     Mengembalikan titik-titik yang membentuk kurva bezier
#     """
#     if iterations == 0:
#         return points
#     else:
#         new_points = []
#         for i in range(len(points) - 1):
#             new_points.append(midpoint(points[i], points[i + 1]))
#         return bezier(new_points, iterations - 1)
    
def bezier(points, iterations, all_points=None):
    """
    Membagi titik kontrol menjadi dua bagian dan menghitung titik tengah
    Hingga jumlah iterasi yang diberikan tercapai
    Mengembalikan titik-titik yang membentuk kurva bezier
    """
    if all_points is None:
        all_points = []
    all_points.extend(points)
    if iterations == 0:
        return all_points
    else:
        new_points = []
        for i in range(len(points) - 1):
            new_points.append(midpoint(points[i], points[i + 1]))
        return bezier(new_points, iterations - 1, all_points)

def plot_bezier_curve(points, iterations):
    """
    Menampilkan kurva bezier dengan control points dan iterasi yang diberikan
    """
    start_time = time.time()
    bezier_points = bezier(points, iterations)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000

    plt.plot(*zip(*points), label="Control Points", marker='o', linestyle='-', color='r')
    plt.plot(*zip(*bezier_points), label="Bezier Curve", marker='o', linestyle='-', color='b')
    plt.title(f"Bezier Curve with {len(points)} Control Points and {iterations} Iterations")
    plt.legend()
    plt.show()

    print(f"Execution time: {execution_time} ms")

def main():
    points = []
    n = int(input("Enter the number of control points: "))
    for i in range(n):
        x, y = map(float, input(f"Enter the x and y coordinates of point {i + 1}: ").split())
        points.append((x, y))
    iterations = int(input("Enter the number of iterations: "))

    # Menampilkan kurva bezier
    plot_bezier_curve(points, iterations)

if __name__ == "__main__":
    main()