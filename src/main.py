import bruteForceBezierCurve as bfbc
import time 
def main():
    # Mengambil input dari pengguna untuk titik kontrol
    num_control_points = int(input("Masukkan jumlah titik kontrol: "))
    control_points = []
    for i in range(num_control_points):
        x = float(input(f"Masukkan koordinat x untuk titik kontrol {i+1}: "))
        y = float(input(f"Masukkan koordinat y untuk titik kontrol {i+1}: "))
        control_points.append((x, y))
    print(control_points)
    # bezier_points = bfbc.bezier_curve_recursive(control_points, 0.5)
    # print("bezier points", bezier_points)
    # Mengatur jumlah titik yang akan diplot
    num_points = 1000

    # Time and plot the curve
    start_time = time.time()
    plot_bezier(control_points, num_points)
    end_time = time.time()

    # Print execution time
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Execution time: {execution_time:.2f} ms")

if __name__ == "__main__":
    main()
   