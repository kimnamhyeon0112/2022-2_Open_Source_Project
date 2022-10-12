from calendar import c
from re import T
import re
import calcpkg

print(calcpkg.operation.add(10, 20))
print(calcpkg.operation.mul(10, 20))

print(calcpkg.geometry.triangle_area(30, 40))
print(calcpkg.geometry.rectangle_area(30, 40))
print()

from calcpkg import *

print(add(10, 20))
print(mul(10, 20))

print(triangle_area(30, 40))
print(rectangle_area(30, 40))
print()

import calcpkg

print(calcpkg.add(10, 20))
print(calcpkg.mul(10, 20))
print(geometry.triangle_area(30, 40))
print(geometry.rectangle_area(30, 40))