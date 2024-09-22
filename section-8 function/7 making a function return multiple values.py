def circle(r):
    area = 3.14 * r * r
    circleference = 2 * 3.14 * r

    return area,circleference


a,c = circle(10)
print(f'Area of the circle is {a}, circumference of the circle is {c}')