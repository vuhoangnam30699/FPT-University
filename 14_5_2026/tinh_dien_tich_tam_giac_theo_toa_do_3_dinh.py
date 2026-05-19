def area3(p1, p2, p3):
    
    
    x1, y1 = p1 # tọa độ p1(x1, y1)
    x2, y2 = p2 # tọa độ p2(x2, y2)
    x3, y3 = p3 # tọa độ p3(x3, y3)
    
    s = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return s

A = (15, 0)
B = (0, 36)
C = (99, 0)

print(area3(A, B, C))