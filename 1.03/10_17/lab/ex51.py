# 1) Write a definition for a class named Circle with attributes center and
# radius,where center is a Point tuple and radius is a number
import math

class Circle:
    def __init__(self, center, radius):
         self.center = center
         self.radius = radius


# 2) Instantiate a Circle object that represents a circle with
# its center at (150, 100) and radius 75
        

circ = Circle((150, 100), 75)

# 3) Write a function named point_in_circle that takes a
# Circle and a Point and returns True if the
# Point lies in or on the boundary of the circle.
# DOCS: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle

def point_in_circle(circle, point):
    dis = math.sqrt((point[0] - circle.center[0]) ** 2 + 
                    (point[1] - circle.center[1]) ** 2)
    return dis <= circle.radius

check_point = (300, 100)
inside = point_in_circle(circ, check_point)
print(f"Point {check_point} is in circle: {inside}")
