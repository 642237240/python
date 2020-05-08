import math
import copy


class Point(object):
    '''Represents a point in 2-D space.'''


print(Point)

blank = Point()
print(blank)
blank.x = 3.0
blank.y = 4.0
print(blank.y)
x = blank.x
print(x)
print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


print_point(blank)
# print(blank)


def distance_between_points(a, b):
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)


a = Point()
b = Point()
a.x = 3
a.y = 4
b.x = 6
b.y = 8
print('distance_between_points(a, b)=%f' % distance_between_points(a, b))


class Rectangle(object):
    '''Represents a rectangle.

    attibutes: width, height, corner.
    '''


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p


center = find_center(box)
print_point(center)


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


print(box.width)
print(box.height)
grow_rectangle(box, 50, 100)
print(box.width)
print(box.height)
p2 = copy.copy(blank)
print_point(p2)
print(blank is p2)
print(blank == p2)  # False
box2 = copy.copy(box)   # copy
print(box2 is box)           # False
print(box2.corner is box.corner)    # True
box3 = copy.deepcopy(box)
print(box3 is box)           # False
print(box3.corner is box.corner)    # False
# print(blank.z)
type(blank)
print(hasattr(blank, 'x'))
print(hasattr(blank, 'z'))
