import pytest
import math
from geometry.shapes import Square, Circle
from geometry.utils import area_stats

square = Square(67)
circle = Circle(23)

print(square.area)
print(circle.area)

print(area_stats(square, circle))