from tkinter import *
from functools import cmp_to_key
from itertools import combinations
from collections import deque
import math

#------------------------------------------GrahamScan-----------------------------------------------------------------------------

class GrahamScanApp:
    def __init__(self):
        self.root = root
        win = Toplevel(self.root)
        self.root.title("Graham's Scan Convex Hull Visualizer")

        self.canvas = Canvas(win, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        self.points = []
        self.convex_hull = []

        self.canvas.bind("<Button-1>", self.add_point)
        self.run_button = Button(win, text="Run Graham's Scan", command=self.run_grahams_scan)
        self.run_button.pack()

        # Draw x-axis and y-axis
        self.canvas.create_line(50, 200, 550, 200, width=2)  # x-axis
        self.canvas.create_line(300, 50, 300, 350, width=2)  # y-axis

        # Label x-axis
        for i in range(-10, 11):
            x = 300 + i * 25
            self.canvas.create_text(x, 210, text=str(i), anchor=N)

        # Label y-axis
        for i in range(-8, 9):
            y = 200 - i * 25
            self.canvas.create_text(290, y, text=str(i), anchor=E)

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

    def draw_convex_hull(self):
        self.canvas.delete("convex_hull")
        for i in range(len(self.convex_hull)):
            x1, y1 = self.convex_hull[i]
            x2, y2 = self.convex_hull[(i + 1) % len(self.convex_hull)]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags="convex_hull")

    def run_grahams_scan(self):
        if len(self.points) < 3:
            return

        self.convex_hull = self.graham_scan(self.points)
        self.draw_convex_hull()

    def graham_scan(self, points):
        def cmp_to_origin(p1, p2):
            angle1 = math.atan2(p1[1] - min_y, p1[0] - min_x)
            angle2 = math.atan2(p2[1] - min_y, p2[0] - min_x)
            return 1 if angle1 - angle2 > 0 else -1 if angle1 - angle2 < 0 else 0

        min_point = min(points, key=lambda p: (p[1], p[0]))
        min_x, min_y = min_point

        sorted_points = sorted(points, key=cmp_to_key(cmp_to_origin))

        convex_hull = [sorted_points[0], sorted_points[1]]
        for point in sorted_points[2:]:
            while len(convex_hull) > 1 and self.orientation(convex_hull[-2], convex_hull[-1], point) != 2:
                convex_hull.pop()
            convex_hull.append(point)

        return convex_hull

    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2    
    

#------------------------------------------------Grahamscan----------------------------------------------------------------------


#------------------------------------------------Jarvis March--------------------------------------------------------------------
class JarvisMarchApp:
    def __init__(self):
        self.root = root
        win = Toplevel(self.root)
        self.root.title("Jarvis March Convex Hull Visualizer")

        self.canvas = Canvas(win, width=600, height=400, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)

        self.points = []
        self.convex_hull = []

        self.canvas.bind("<Button-1>", self.add_point)
        self.run_button = Button(win, text="Run Jarvis March", command=self.run_jarvis_march)
        self.run_button.pack()

        # Draw x-axis and y-axis
        self.canvas.create_line(50, 200, 550, 200, width=2)  # x-axis
        self.canvas.create_line(300, 50, 300, 350, width=2)  # y-axis

        # Label x-axis
        for i in range(-10, 11):
            x = 300 + i * 25
            self.canvas.create_text(x, 210, text=str(i), anchor=N)

        # Label y-axis
        for i in range(-8, 9):
            y = 200 - i * 25
            self.canvas.create_text(290, y, text=str(i), anchor=E)

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

    def draw_convex_hull(self):
        self.canvas.delete("convex_hull")
        for i in range(len(self.convex_hull)):
            x1, y1 = self.convex_hull[i]
            x2, y2 = self.convex_hull[(i + 1) % len(self.convex_hull)]
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=2, tags="convex_hull")

    def run_jarvis_march(self):
        if len(self.points) < 3:
            return

        self.convex_hull = self.jarvis_march(self.points)
        self.draw_convex_hull()

    def jarvis_march(self, points):
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else 2

        n = len(points)
        hull = []

        # Find the leftmost point
        leftmost = min(points, key=lambda p: p[0])
        hull.append(leftmost)

        while True:
            endpoint = points[0]
            for i in range(1, n):
                if endpoint == hull[-1] or orientation(hull[-1], points[i], endpoint) == 2:
                    endpoint = points[i]

            if endpoint == hull[0]:
                break

            hull.append(endpoint)

        return hull

#------------------------------------------------Jarvis March--------------------------------------------------------------------


#------------------------------------------------BruteForce--------------------------------------------------------------------
class BruteForceConvexHullApp:
    def __init__(self):
        self.root = root
        win = Toplevel(self.root)
        self.root.title("Brute Force Convex Hull Visualizer")

        self.canvas = Canvas(win, width=600, height=400, bg="#F0F0F0")
        self.canvas.pack(expand=YES, fill=BOTH)

        self.points = []
        self.convex_hull = []

        self.canvas.bind("<Button-1>", self.add_point)
        self.run_button = Button(win, text="Run Brute Force", command=self.run_brute_force)
        self.run_button.pack()

        self.draw_axes()

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

    def draw_axes(self):
        # Draw x-axis
        self.canvas.create_line(50, 200, 550, 200, width=2, arrow=LAST)
        for i in range(-10, 11):
            x = 300 + i * 25
            self.canvas.create_line(x, 198, x, 202, width=2)
            self.canvas.create_text(x, 210, text=str(i), anchor=N)

        # Draw y-axis
        self.canvas.create_line(300, 50, 300, 350, width=2, arrow=LAST)
        for i in range(-8, 9):
            y = 200 - i * 25
            self.canvas.create_line(298, y, 302, y, width=2)
            self.canvas.create_text(290, y, text=str(i), anchor=E)

    def draw_convex_hull(self):
        self.canvas.delete("convex_hull")
        for i in range(len(self.convex_hull)):
            x1, y1 = self.convex_hull[i]
            x2, y2 = self.convex_hull[(i + 1) % len(self.convex_hull)]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags="convex_hull")

    def run_brute_force(self):
        if len(self.points) < 3:
            return

        self.convex_hull = self.brute_force(self.points)
        self.draw_convex_hull()

    def brute_force(self, points):
        def is_ccw(p1, p2, p3):
            return (p3[1] - p1[1]) * (p2[0] - p1[0]) > (p2[1] - p1[1]) * (p3[0] - p1[0])

        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
               return 0
            return 1 if val > 0 else -1

        def on_segment(p, q, r):
            return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                    q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

        convex_hull = []

        for combo in combinations(self.points, 3):
            p1, p2, p3 = combo
            valid = True

            for point in points:
                if point not in combo:
                    if not is_ccw(p1, p2, point) and not is_ccw(p2, p3, point) and not is_ccw(p3, p1, point):
                        valid = False
                        break

            if valid:
                convex_hull.extend(combo)

        # Sort the convex hull points by angle
        convex_hull.sort(key=lambda p: (p[0], p[1]))

        return convex_hull


#------------------------------------------------BruteForce--------------------------------------------------------------------



#------------------------------------------------Lineintersection--------------------------------------------------------------------
class LineIntersectionApp:
    def __init__(self):
        self.root = root
        win = Toplevel(self.root)
        self.root.title("Line Intersection Visualizer")

        # Change the background color here
        self.canvas = Canvas(win, width=600, height=400, bg="#F0F0F0")
        self.canvas.pack(expand=YES, fill=BOTH)

        self.lines = []

        self.canvas.bind("<Button-1>", self.add_point)
        self.run_button = Button(win, text="Show Intersections", command=self.show_intersections)
        self.run_button.pack()

        # Draw x-axis and y-axis
        self.canvas.create_line(50, 200, 550, 200, width=2)  # x-axis
        self.canvas.create_line(300, 50, 300, 350, width=2)  # y-axis

        # Label x-axis
        for i in range(-10, 11):
            x = 300 + i * 25
            self.canvas.create_text(x, 210, text=str(i), anchor=N)

        # Label y-axis
        for i in range(-8, 9):
            y = 200 - i * 25
            self.canvas.create_text(290, y, text=str(i), anchor=E)

    def add_point(self, event):
        x, y = event.x, event.y
        self.lines.append([(x, y), None])
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

        if len(self.lines) % 2 == 0:
            self.canvas.create_line(self.lines[-2][0], self.lines[-1][0])

    def show_intersections(self):
        self.canvas.delete("intersections")

        for i in range(0, len(self.lines), 2):
            for j in range(i + 2, len(self.lines), 2):
                intersection = self.get_line_intersection(self.lines[i][0], self.lines[i + 1][0],
                                                           self.lines[j][0], self.lines[j + 1][0])

                if intersection:
                    x, y = intersection
                    self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red", tags="intersections")

    @staticmethod
    def get_line_intersection(p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if denominator == 0:
            return None  # Lines are parallel

        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator

        return px, py


#------------------------------------------------Lineintersection--------------------------------------------------------------------


#------------------------------------------------DynamicPlanar--------------------------------------------------------------------
class DynamicConvexHullApp:
    def __init__(self):
        self.root = root
        win = Toplevel(self.root)
        self.root.title("Dynamic Convex Hull Visualizer")

        self.canvas = Canvas(win, width=600, height=400, bg="#F0F0F0")
        self.canvas.pack(expand=YES, fill=BOTH)

        self.points = deque()
        self.convex_hull = deque()

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.remove_point)
        self.run_button = Button(win, text="Run Convex Hull", command=self.run_convex_hull)
        self.run_button.pack()

        self.draw_axes()

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

        # Update convex hull
        self.update_convex_hull()

    def remove_point(self, event):
        x, y = event.x, event.y

        if not self.points:
            return

        closest_point = min(self.points, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)
        self.points.remove(closest_point)

        # Redraw everything
        self.canvas.delete("all")
        self.draw_axes()
        self.draw_points()

        # Update convex hull
        self.update_convex_hull()

    def draw_points(self):
        for x, y in self.points:
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")

    def draw_axes(self):
        # Draw x-axis
        self.canvas.create_line(50, 200, 550, 200, width=2, arrow=LAST)
        for i in range(-10, 11):
            x = 300 + i * 25
            self.canvas.create_line(x, 198, x, 202, width=2)
            self.canvas.create_text(x, 210, text=str(i), anchor=N)

        # Draw y-axis
        self.canvas.create_line(300, 50, 300, 350, width=2, arrow=LAST)
        for i in range(-8, 9):
            y = 200 - i * 25
            self.canvas.create_line(298, y, 302, y, width=2)
            self.canvas.create_text(290, y, text=str(i), anchor=E)

    def draw_convex_hull(self):
        self.canvas.delete("convex_hull")
        for i in range(len(self.convex_hull)):
            x1, y1 = self.convex_hull[i]
            x2, y2 = self.convex_hull[(i + 1) % len(self.convex_hull)]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags="convex_hull")

    def run_convex_hull(self):
        # Update convex hull
        self.update_convex_hull()

    def update_convex_hull(self):
        if len(self.points) < 5:
            return

        # Sort points by x-coordinate, then by y-coordinate
        sorted_points = sorted(self.points, key=lambda p: (p[0], p[1]))

        upper_hull = deque()
        lower_hull = deque()

        # Build upper and lower hulls
        for p in sorted_points:
            while len(upper_hull) >= 2 and self.orientation(upper_hull[-2], upper_hull[-1], p) != 1:
                upper_hull.pop()
            upper_hull.append(p)

            while len(lower_hull) >= 2 and self.orientation(lower_hull[-2], lower_hull[-1], p) != -1:
                lower_hull.pop()
            lower_hull.append(p)

        # Combine upper and lower hulls to get the convex hull
        self.convex_hull = upper_hull + lower_hull

        # Draw convex hull
        self.draw_convex_hull()

    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else -1
#------------------------------------------------DynamicPlanar--------------------------------------------------------------------

#------------------------------------------------Quick Elimination----------------------------------------------------------------
class QuickeliminationApp:
    def __init__(self):
        self.points = []
        self.convex_hull = []

        self.root=root
        win = Toplevel(self.root)
        self.root.title("QuickHull Visualization")

        self.canvas = Canvas(win, width=600, height=400, bg="white")
        self.canvas.pack()

        # Draw x-axis
        self.canvas.create_line(50, 200, 550, 200, width=2, arrow=LAST)
        for i in range(-10, 11):
            x = 300 + i * 25
            self.canvas.create_line(x, 198, x, 202, width=2)
            self.canvas.create_text(x, 210, text=str(i), anchor=N)

        # Draw y-axis
        self.canvas.create_line(300, 50, 300, 350, width=2, arrow=LAST)
        for i in range(-8, 9):
            y = 200 - i * 25
            self.canvas.create_line(298, y, 302, y, width=2)
            self.canvas.create_text(290, y, text=str(i), anchor='e')
     

        self.canvas.bind("<Button-1>", self.add_point)
        self.btn_quick_hull = Button(win, text="QuickHull", command=self.run_quick_hull)
        self.btn_quick_hull.pack()
    
    def distance(self,p1, p2, p3):
     return abs((p2[0] - p1[0]) * (p1[1] - p3[1]) - (p1[0] - p3[0]) * (p2[1] - p1[1]))
    
    def is_right(self, p1, p2, p3):
       return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]) < 0
    
    def add_point(self,event):
     x, y = event.x, event.y
     self.points.append((x, y))
     self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

    def quick_hull(self,points):
        def find_hull(p1, p2, points):
          sub_hull = [point for point in points if self.is_right(p1, p2, point)]
          if not sub_hull:
              return [p1, p2]

          furthest_point = max(sub_hull, key=lambda point: self.distance(p1, p2, point))
          return find_hull(p1, furthest_point, sub_hull) + find_hull(furthest_point, p2, sub_hull)

        if len(points) < 3:
         return points

        leftmost = min(points, key=lambda p: p[0])
        rightmost = max(points, key=lambda p: p[0])

        upper_hull = find_hull(leftmost, rightmost, points)
        lower_hull = find_hull(rightmost, leftmost, points)

        return upper_hull + lower_hull[1:-1]

    def run_quick_hull(self):
      global convex_hull
      convex_hull = self.quick_hull(self.points)

      self.canvas.delete("all")
      for x, y in self.points:
         self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

      self.draw_convex_hull(convex_hull)

    def draw_convex_hull(self,hull):
       self.canvas.delete("convex_hull")
       for i in range(len(hull) - 1):
         x1, y1 = hull[i]
         x2, y2 = hull[i + 1]
         self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags=("convex_hull",))

       if hull:
         x1, y1 = hull[-1]
         x2, y2 = hull[0]
         self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags=("convex_hull",))


#------------------------------------------------Quick Elimination---------------------------------------------------------------

#------------------------------------------------LineIntersection By CCW---------------------------------------------------------
class LineIntersectionAppCcw:
    def __init__(self):
        self.root = root
        win = Toplevel(self.root)
        self.root.title("Line Intersection Checker")

        self.canvas = Canvas(win, width=600, height=400, bg="white")
        self.canvas.pack()

        # Draw X and Y axes
        # Draw x-axis
        self.canvas.create_line(50, 200, 550, 200, width=2, arrow=LAST)
        for i in range(-10, 11):
            x = 300 + i * 25
            self.canvas.create_line(x, 198, x, 202, width=2)
            self.canvas.create_text(x, 210, text=str(i), anchor=N)

        # Draw y-axis
        self.canvas.create_line(300, 50, 300, 350, width=2, arrow=LAST)
        for i in range(-8, 9):
            y = 200 - i * 25
            self.canvas.create_line(298, y, 302, y, width=2)
            self.canvas.create_text(290, y, text=str(i), anchor='e')

        self.lines = []
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.result_label = Label(win, text="")
        self.result_label.pack(pady=10)

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        self.lines.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="black")

        if len(self.lines) >= 4:
            intersect = self.do_intersect((self.lines[-4], self.lines[-3]), (self.lines[-2], self.lines[-1]))
            result_text = "Lines intersect!" if intersect else "Lines do not intersect."
            self.result_label.config(text=result_text)

    def ccw(self, A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    def do_intersect(self, seg1, seg2):
        A, B = seg1
        C, D = seg2
        ccw1 = self.ccw(A, C, D) != self.ccw(B, C, D)
        ccw2 = self.ccw(A, B, C) != self.ccw(A, B, D)
        return ccw1 and ccw2        
           

#------------------------------------------------LineIntersection By CCW--------------------------------------------------------
root = Tk()
#         window title
root.title('GEOMETRIC ALGORITHMS PROJECT')

#         window dimensions (FIXED)
root.geometry('1000x700')
root.resizable(0,0)

#         window background color
root.configure(background='black')

#         MAIN HEADING
heading_label= Label(root, text='WELCOME TO OUR ALGORITHM PROJECT',fg='white',bg='black')
heading_label.config(font=('halvetica',20,'bold'))
heading_label.pack(pady=(20,20))

#         GROUP MEMBERS LABELING
member_label= Label(root, text='GROUP MEMBERS',fg='white',bg='black')
member_label.config(font=('arial',12,'bold'))
member_label.pack(pady=(10,10))
first_label= Label(root, text='21k-3424',fg='red',bg='black')
second_label= Label(root, text='21k-3280',fg='red',bg='black')
third_label= Label(root, text='21k-4840',fg='red',bg='black')
first_label.config(font=('arial',10,'bold','italic'))
second_label.config(font=('arial',10,'bold','italic'))
third_label.config(font=('arial',10,'bold','italic'))
first_label.pack()
second_label.pack()
third_label.pack()

#         Listing algorithms
algo_label= Label(root, text='Select Any Algorithm That You Wish To Implement',fg='white',bg='black')
algo_label.config(font=('arial',14,'bold'))
algo_label.pack(pady=(20,10))

line_but= Button(root,text='LINE INTERSECTION',fg='red',bg='black',command=LineIntersectionApp)
line_but.config(font=('times new roman',12,'bold'))
line_but.pack(pady=(7,7))

line_sec_but= Button(root,text='LINE INTERSECTION BY CCW',fg='red',bg='black',command=LineIntersectionAppCcw)
line_sec_but.config(font=('times new roman',12,'bold'))
line_sec_but.pack(pady=(7,7))

bruteforce_but= Button(root,text='BRUTE FORCE',fg='red',bg='black',command=BruteForceConvexHullApp)
bruteforce_but.config(font=('times new roman',12,'bold'))
bruteforce_but.pack(pady=(7,7))

jarvis_but= Button(root,text='JARVIS MARCH',fg='red',bg='black',command=JarvisMarchApp)
jarvis_but.config(font=('times new roman',12,'bold'))
jarvis_but.pack(pady=(7,7))

graham_but= Button(root,text='GRAHAMSCAN',fg='red',bg='black',command=GrahamScanApp)
graham_but.config(font=('times new roman',12,'bold'))
graham_but.pack(pady=(7,7))

quick_but= Button(root,text='QUICK ELIMINATION',fg='red',bg='black', command=QuickeliminationApp)
quick_but.config(font=('times new roman',12,'bold'))
quick_but.pack(pady=(7,7))

dynamic_but= Button(root,text='DYNAMIC PLANAR',fg='red',bg='black',command=DynamicConvexHullApp)
dynamic_but.config(font=('times new roman',12,'bold'))
dynamic_but.pack(pady=(7,7))

root.mainloop()