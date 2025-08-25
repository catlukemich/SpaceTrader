import math

class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        result = Vector2(self.x, self.y)
        result.x += other.x
        result.y += other.y
        return result

    def __sub__(self, other):
        result = Vector2(self.x, self.y)
        result.x -= other.x
        result.y -= other.y
        return result

    def __mul__(self, val):
        result = Vector2(self.x, self.y)
        result.x *= val
        result.y *= val
        return result

    def __truediv__(self, val):
        result = Vector2(self.x, self.y)
        result.x /= val
        result.y /= val
        return result

    # Clockwise rotation
    def rotate(self, angle):
        rads = math.radians(-angle)
        x = self.x * math.cos(rads) - self.y * math.sin(rads)
        y = self.x * math.sin(rads) + self.y * math.cos(rads)

        self.x = x
        self.y = y

        return self
    
    def rotated(self, angle):
        rads = math.radians(-angle)
        x = self.x * math.cos(rads) - self.y * math.sin(rads)
        y = self.x * math.sin(rads) + self.y * math.cos(rads)
        result = Vector2(x, y)
        return result

    def length(self):
        l = math.sqrt(self.x ** 2 + self.y ** 2)
        return l

    def normalize(self):
        l = self.length()
        self.x = self.x  / l
        self.y = self.y  / l
        return self

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist
    
    def asTuple(self):
        return (self.x, self.y)

    def distancePointToLine(self, direction, point):
        # wektor PA
        dx, dy = point.x - self.x, point.y - self.y
        # iloczyn wektorowy 2D (to skalar)
        cross = abs(dx * direction.y - dy * direction.x)
        # norma wektora kierunkowego
        norm_v = math.hypot(direction.x, direction.y)
        return cross / norm_v
    
    def __str__(self):
        return f"vec2 {self.x}, {self.y}"



def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def clamp(value, min, max):
    if value < min:
        value = min
    if value > max:
        value = max
    return value




if __name__ == "__main__":
    v1 = Vector2(0,1)
    v1.rotate(45)
    v2 = Vector2(1,1)
    v2.normalize()

