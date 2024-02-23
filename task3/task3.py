import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self):
        return f"<Point({self.x}, {self.y})>"


def isCorrectTriangle(p1, p2, p3):
    a = p1.distance_to(p2)
    b = p2.distance_to(p3)
    c = p3.distance_to(p1)
    return a + b > c and a + c > b and b + c > a


def heron(p1, p2, p3):
    a = p1.distance_to(p2)
    b = p2.distance_to(p3)
    c = p3.distance_to(p1)
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def max_area_of_triangle(points):
    max_area = 0
    max_triangles = []
    triangle = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                triangle.append(points[i])
                triangle.append(points[j])
                triangle.append(points[k])
                if isCorrectTriangle(triangle[0], triangle[1], triangle[2]):
                    area = round( heron(triangle[0], triangle[1], triangle[2]),5)
                    if area > max_area:
                        max_triangles = [triangle]
                        max_area = area
                    elif area == max_area:
                        max_triangles.append(triangle)
                triangle = []
    return max_area, random.choice(max_triangles)


def main():
    with open('test_task_3.txt', 'r') as file:
        lines = file.readlines()
        list_of_points = []
        for line in lines:
            if line.strip():
                x, y = map(float, line.strip().split())
                list_of_points.append(Point(x, y))

    max_area, max_triangle = max_area_of_triangle(list_of_points)
    print(max_area)
    print(max_triangle)

    with open('answer_task_3.txt', 'w') as file:
        file.write(str(max_triangle))


if __name__ == "__main__":
    main()
