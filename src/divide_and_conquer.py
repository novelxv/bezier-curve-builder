import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def midpoint(point1, point2):
    """ 
    Returns the midpoint between two points
    """
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2

def insert_midpoints(arr, midpoints):
    """
    Inserts midpoints into in between the elements of the array
    """
    for i in range(len(arr) - 1, 0, -1):
        arr.insert(i, midpoints[i - 1])
    return arr

def bezier(control_points, all_points, iterations):
    """
    Constructs the Bezier curve points using the midpoint algorithm for the given iteration
    """
    if iterations == 0:
        return all_points
    else:
        # Calculate the midpoints
        mid1 = []
        for i in range(1, len(control_points)):
            mid1.append(midpoint(control_points[i-1], control_points[i]))
        all_points.append(mid1)
        # Calculate the midpoints of the midpoints
        mid2 = []
        for i in range(1, len(mid1)):
            mid2.append(midpoint(mid1[i-1], mid1[i]))
        # If it's already the last iteration, add the curve's points to the list and return
        if iterations == 1:
            curve = []
            curve.append(control_points[0])
            curve.extend(mid2)
            curve.append(control_points[-1])
            all_points.append(curve)
            return all_points
        # Insert both midpoints lists as new control points for the next iteration
        new_control_points = []
        new_control_points.append(control_points[0])
        new_control_points.extend(insert_midpoints(mid1, mid2))
        new_control_points.append(control_points[-1])
        # Recursively call the function for the next iteration
        return bezier(new_control_points, all_points, iterations - 1)
    
def plot_bezier_divide_and_conquer(control_points, iteration):
    start_time = time.time()
    """ Plots the Bezier curve using the midpoint algorithm for a given set of control points and iterations. """
    bezier_points = bezier(control_points, [control_points], iteration)[-1]
    # Extract x and y coordinates from points
    x_values, y_values = zip(*bezier_points)
    control_x, control_y = zip(*control_points)
    
    with plt.style.context('dark_background'):
        plt.figure()
        plt.plot(x_values, y_values, 'm-', label='Bezier Curve')
        plt.plot(control_x, control_y, 'o--', label='Control Points', color='cyan', markersize=0.5)
        plt.title(f'Bezier Curve with {iteration} iterations')
        plt.legend()

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nExecution time: {execution_time:.2f} ms")
    
    plt.show()
        
def plot_bezier_divide_and_conquer_animate(control_points, iterations):
    """
    Plots and animates the Bezier curve using the given control points and iterations
    """
    start_time = time.time()

    all_points = [control_points]
    all_points = bezier(control_points, all_points, iterations) # all points to be animated
    total_frames = sum(len(group) for group in all_points) # total frames needed for the animation

    colors = ['blue', '#FF007F', '#9400D3', '#FF69B4', '#00FFFF', '#FFFF33'] # colors for each group

    with plt.style.context('dark_background'):
        fig, ax = plt.subplots()

    # Adjust the xlim and ylim boundaries based on the available points for the best view
    xlim_max = max([x for x, y in control_points]) + 1
    xlim_min = min([x for x, y in control_points]) - 1
    ylim_max = max([y for x, y in control_points]) + 1
    ylim_min = min([y for x, y in control_points]) - 1
    ax.set_xlim(xlim_min, xlim_max)
    ax.set_ylim(ylim_min, ylim_max)

    # Create line objects for each group of points
    lines = []
    for i, _ in enumerate(all_points):
        line_style = 'o--' if i != len(all_points) - 1 else 'o-'
        color = colors[i % len(colors)]
        label = 'Control Points & Bezier Curve' if i == 0 and len(all_points) - 1 == 0 else 'Bezier Curve' if i == len(all_points) - 1 else 'Control Points' if i == 0 else None
        line = ax.plot([], [], line_style, color=color, markersize=3, label=label)[0]
        lines.append(line)
    # Initialize the line objects
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    # Animate the line objects
    def animate(frame):
        total_points_drawn = 0 # Total points already drawn
        for group_index, points in enumerate(all_points):
            # Calculate the total points up to the current group
            total_points_up_to_current_group = sum(len(group) for group in all_points[:group_index + 1])
            if frame < total_points_up_to_current_group:
                # Number of points drawn for the current group
                num_points_in_current_group = frame - total_points_drawn
                drawn_points = points[:num_points_in_current_group + 1]
                lines[group_index].set_data(*zip(*drawn_points))
                break # Exit the loop because the current group is being drawn
            else:
                # Draw all points in this group because the frame exceeds the total number of points in this group
                lines[group_index].set_data(*zip(*points))
                total_points_drawn = total_points_up_to_current_group

        return lines

    # Make the animation object
    anim = FuncAnimation(fig, animate, frames=total_frames, init_func=init, blit=True, interval=1000)

    ax.legend()

    plt.title(f'Bezier Curve with {iterations} iterations')

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000 # Convert to milliseconds
    print(f"\nExecution time: {execution_time:.2f} ms")

    plt.show()

def display_welcome_message():
    print("================================================")
    print("  Welcome to the Bézier Curve Animator ✨✨✨ ")
    print("================================================")
    print("\nThis program allows you to animate the formation of Bézier curves using the Divide and Conquer method.")
    print("\nPlease follow the prompts to input your control points and number of iterations.")
    print("\nLet's get started!\n")

def main():
    display_welcome_message()
    # Take input from the user for the control points
    control_points = []
    n = int(input("Enter the number of control points: "))
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

    # Plot the Bezier curve
    # ask user if they want to animate the curve
    print("\nDo you want to animate the curve? (y/n)")
    animate = input().lower()
    if animate == 'y':
        plot_bezier_divide_and_conquer_animate(control_points, iterations)
    else:
        plot_bezier_divide_and_conquer(control_points, iterations)

    print("\nGoodbye! Hope you enjoyed the bezier curve 💞")

if __name__ == "__main__":
    main()