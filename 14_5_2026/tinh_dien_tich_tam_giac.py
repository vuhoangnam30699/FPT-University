import math

def area(a, b, c):
    
    # p là nửa chu vi
    p = (a + b + c) / 2
    
    # Công thức Heron
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    return s


print(area(3, 4, 5))