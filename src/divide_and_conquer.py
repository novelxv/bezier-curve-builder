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
        
def plot_midpoint_bezier(control_points, all_points, iterations):
    """
    Plots and animates the Bezier curve using the given control points and iterations
    """
    all_points = bezier(control_points, all_points, iterations) # all points to be animated
    total_frames = sum(len(group) for group in all_points) # total frames needed for the animation

    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow'] # colors for each group

    fig, ax = plt.subplots()

    # Adjust the xlim and ylim boundaries based on the available points for the best view
    xlim_max = max([x for x, y in control_points]) + 2
    xlim_min = min([x for x, y in control_points]) - 2
    ylim_max = max([y for x, y in control_points]) + 2
    ylim_min = min([y for x, y in control_points]) - 2
    ax.set_xlim(xlim_min, xlim_max)
    ax.set_ylim(ylim_min, ylim_max)

    # Create line objects for each group of points
    lines = []
    for i, _ in enumerate(all_points):
        line_style = 'o--' if i != len(all_points) - 1 else 'o-'
        color = colors[i % len(colors)]
        label = 'Control Points' if i == 0 else 'Bezier Curve' if i == len(all_points) - 1 else None
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

    plt.show()


def main():

    control_points = []
    n = int(input("Enter the number of control points: "))
    for i in range(n):
        x, y = map(float, input(f"Enter the x and y coordinates of point {i + 1}: ").split())
        control_points.append((x, y))
    iterations = int(input("Enter the number of iterations: "))
    all_points = [control_points]

    plot_midpoint_bezier(control_points, all_points, iterations)

if __name__ == "__main__":
    main()