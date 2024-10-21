import data

# Write your functions for each part in the space below.

# Part 1
def first_element(robFirst:list[list[int]]) -> list:
    firstValues = []
    for x in robFirst:
        firstValues.append(x[0])
    return firstValues

# Part 2
def x_coordinates(points:list) -> list:
    xCords = []
    for x in points:
        xCords.append(x[0])
    return xCords

# Part 3
def are_in_positive_quadrant(points:list)-> list:
    positive_Quadrant = []
    for x in points:
        if x[0] > 0 and x[1] > 0:
            positive_Quadrant.append(x)
    return positive_Quadrant

# Part 4
def distance(point1:list[float], point2:list[float]) -> float:
    distance_answer = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
    return round(distance_answer,2)

# Part 5
def manhattan_distance(point1:list[float], point2:list[float]) -> float:
    m_distance_answer = abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
    return m_distance_answer


# Part 6
def distance_all(points:list) -> list[int]:
    distance_formula = []
    for x in points:
        distance_formula.append(((0 - x[0]) ** 2 + (0 - x[1]) ** 2) ** 0.5)
    return distance_formula