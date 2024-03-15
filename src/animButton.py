import tkinter as tk
from tkinter import simpledialog, messagebox

class BezierAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()
        self.points = []
        self.midpoints = []
        self.curve = None
        self.curve_color = "blue"
        self.point_radius = 4
        self.control_point_count = 0
        self.control_point_button = tk.Button(master, text="Set Control Points", command=self.set_control_points)
        self.control_point_button.pack()

    def set_control_points(self):
        count = int(self.get_control_point_count())
        if count < 2:
            messagebox.showerror("Error", "Please enter at least 2 control points.")
            return
        self.control_point_count = count
        self.clear_canvas()
        self.create_control_point_entries()

    def get_control_point_count(self):
        return simpledialog.askstring("Control Point Count", "Enter the number of control points:")

    def create_control_point_entries(self):
        for i in range(self.control_point_count):
            lbl = tk.Label(self.master, text=f"Point {i + 1}:")
            lbl.pack()
            entry = tk.Entry(self.master)
            entry.pack()
            self.points.append(entry)

        submit_button = tk.Button(self.master, text="Submit", command=self.submit_control_points)
        submit_button.pack()

    def submit_control_points(self):
        try:
            self.points = [(int(entry.get().split(',')[0]), int(entry.get().split(',')[1])) for entry in self.points]
        except ValueError:
            messagebox.showerror("Error", "Invalid input format. Please enter points in the format 'x, y'.")
            return
        self.draw_control_points()
        if len(self.points) > 2:
            self.calculate_midpoints()
            self.draw_bezier_curve()

    def draw_control_points(self):
        for point in self.points:
            x, y = point
            self.canvas.create_oval(x - self.point_radius, y - self.point_radius,
                                    x + self.point_radius, y + self.point_radius,
                                    fill="black")
        for i in range(len(self.points) - 1):
            self.canvas.create_line(self.points[i], self.points[i + 1], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")

    def calculate_midpoints(self):
        self.midpoints = []
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            self.midpoints.append((mid_x, mid_y))

    def draw_bezier_curve(self):
        self.curve = self.canvas.create_line(self.points, fill=self.curve_color)
        self.draw_midpoints()

    def draw_midpoints(self):
        for point in self.midpoints:
            x, y = point
            self.canvas.create_oval(x - self.point_radius / 2, y - self.point_radius / 2,
                                    x + self.point_radius / 2, y + self.point_radius / 2,
                                    fill="red")

def main():
    root = tk.Tk()
    root.title("Bezier Curve Animation")
    BezierAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
