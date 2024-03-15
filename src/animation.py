import tkinter as tk

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
        self.bind_events()
    
    def bind_events(self):
        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.animate)
    
    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - self.point_radius, y - self.point_radius,
                                x + self.point_radius, y + self.point_radius,
                                fill="black")
        if len(self.points) > 1:
            self.canvas.create_line(self.points[-2], self.points[-1], fill="black")
        if len(self.points) > 2:
            self.calculate_midpoints()
            self.draw_bezier_curve()

    def calculate_midpoints(self):
        self.midpoints = []
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            self.midpoints.append((mid_x, mid_y))

    def draw_bezier_curve(self):
        self.canvas.delete(self.curve)
        bezier_points = self.calculate_bezier_points()
        self.curve = self.canvas.create_line(bezier_points, fill=self.curve_color)
        self.draw_midpoints()

    def calculate_bezier_points(self):
        bezier_points = []
        for t in range(101):
            t = t / 100
            x, y = self.calculate_bezier_point(t)
            bezier_points.append(x)
            bezier_points.append(y)
        return bezier_points

    def calculate_bezier_point(self, t):
        n = len(self.points)
        x, y = 0, 0
        for i in range(n):
            b = self.binomial_coefficient(n - 1, i) * (1 - t) ** (n - 1 - i) * t ** i
            x += self.points[i][0] * b
            y += self.points[i][1] * b
        return x, y

    def binomial_coefficient(self, n, k):
        if k == 0 or k == n:
            return 1
        return self.factorial(n) // (self.factorial(k) * self.factorial(n - k))

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def draw_midpoints(self):
        for point in self.midpoints:
            x, y = point
            self.canvas.create_oval(x - self.point_radius / 2, y - self.point_radius / 2,
                                    x + self.point_radius / 2, y + self.point_radius / 2,
                                    fill="red")

    def animate(self, event):
        self.canvas.delete(self.curve)
        for point in self.midpoints:
            self.canvas.delete(self.canvas.create_oval(point[0] - self.point_radius / 2,
                                                        point[1] - self.point_radius / 2,
                                                        point[0] + self.point_radius / 2,
                                                        point[1] + self.point_radius / 2,
                                                        fill="red"))
        self.canvas.update()
        self.animate_bezier(0, 1, 0.01)

    def animate_bezier(self, t_start, t_end, step):
        if t_start >= t_end:
            return
        points = []
        t = t_start
        while t <= t_end:
            x, y = self.calculate_bezier_point(t)
            points.append(x)
            points.append(y)
            t += step
        self.curve = self.canvas.create_line(points, fill=self.curve_color)
        self.canvas.update()
        self.master.after(50, lambda: self.animate_bezier(t_start + step, t_end, step))

def main():
    root = tk.Tk()
    root.title("Bezier Curve Animation")
    BezierAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
