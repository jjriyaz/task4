class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self):
        areas = []
        for radius in self.radius_list:
            area = 3.141 * radius * radius  # Using pi as approximately 3.14159
            areas.append(area)
        return areas

    def calculate_perimeter(self):
        perimeters = []
        for radius in self.radius_list:
            perimeter = 2 * 3.141 * radius  # Using pi as approximately 3.14159
            perimeters.append(perimeter)
        return perimeters

# Example usage:
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radius_list)

areas = circle.calculate_area()
perimeters = circle.calculate_perimeter()

print("Areas:", areas)
print("Perimeters:", perimeters)