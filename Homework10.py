from datetime import datetime
import time

class Point:
    coords = None

    def __init__(self, coord_x, coord_y):
        if not isinstance(coord_x, (int, float)):
            raise TypeError

        if not isinstance(coord_y, (int, float)):
            raise TypeError

        self.coords = (coord_x, coord_y)

    def get_x(self):
        return self.coords[0]

    def get_y(self):
        return self.coords[1]

    def __add__(self, other):
        if type(other) != Point:
            raise TypeError
        return Point(self.coords[0] + other.coords[0], self.coords[1] + other.coords[1])

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError
        return Point(self.coords[0] * other, self.coords[1] * other)

    def __sub__(self, other):
        if type(other) != Point:
            raise TypeError
        return Point(self.coords[0] - other.coords[0], self.coords[1] - other.coords[1])

    def to_str(self, num_of_point):
        return f"Point {num_of_point} ({self.coords[0]}, {self.coords[1]})"

    def __str__(self):
        return f"Point({self.coords[0]}, {self.coords[1]})"


class Line:
    points = []

    def __init__(self, *args):
        self.points = []
        args = list(args)
        for arg in args:
            if type(arg) == list and len(arg) >= 2:
                for point in arg:
                    if type(point) != Point:
                        raise TypeError
                    self.points.append(point)
            elif type(arg) == Point:
                self.points.append(arg)
            else:
                raise TypeError

    def __str__(self):
        txt = "Line. Points:"
        num = 0
        for point in self.points:
            txt += f" {point.to_str(num)},"
            num += 1
        return txt

    def length_getter(self):
        prev_p = None
        l_len = 0
        for point in self.points:
            if prev_p is not None:
                x = (point.get_x() - prev_p.get_x()) ** 2
                y = (point.get_y() - prev_p.get_y()) ** 2
                l_len += (x + y) ** 0.5
            prev_p = point

        return l_len

    def length_setter(self, value):
        value = (value/self.length_getter()) - 1
        counter = 1
        border = len(self.points)
        while counter < border:
            counter2 = counter
            correction = (self.points[counter] - self.points[counter - 1]) * value
            while counter2 < border:
                self.points[counter2] += correction
                counter2 += 1
            counter += 1

    def __getitem__(self, pos):
        return self.points[pos]

    def __setitem__(self, key, value):
        if type(value) != Point:
            raise TypeError
        self.points[key] = value

    def first_point_getter(self):
        return self.points[0]

    def first_point_setter(self, value):
        if type(value) is not Point:
            raise TypeError
        self.points[0] = value

    def last_point_getter(self):
        return self.points[len(self.points) - 1]

    def last_point_setter(self, value):
        if type(value) is not Point:
            raise TypeError
        self.points[len(self.points) - 1] = value

    length = property(length_getter, length_setter)
    first_point = property(first_point_getter, first_point_setter)
    last_point = property(last_point_getter, last_point_setter)


def hard_func():
    time.sleep(5)


def time_checker_decorator(func):
    def wrapper():
        start_time = datetime.now()
        func()
        print(datetime.now() - start_time)
    return wrapper


line = Line(Point(0, 0), Point(4, 0), Point(4, 2))
print(line.length)
line.length = 9
print(line.length)

line = Line(Point(0, 0), Point(2, 2))
print(line.length)
line.first_point = Point(1, 2)
print(line.first_point)

hard_func = time_checker_decorator(hard_func)
hard_func()





