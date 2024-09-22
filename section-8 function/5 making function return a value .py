def area(radius,pi=3.14):
    result = pi*radius*radius
    return result

def cost(circle_area,cost_per_sqm):
    total_cost = circle_area*cost_per_sqm
    return total_cost



tc = cost(area(10,3.15) ,2)
print(tc)


# nasting (shortcut)
print(cost(area(10,3.15) ,2))
