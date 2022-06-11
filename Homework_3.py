class Shape:
    CL_NAME = "SHAPE"

    def __init__(self, side_amount, name):
        print("Here starts Shape init")
        self.side_amount = side_amount
        self.name = name
    print("Here ends Shape init")

    def present(self):
        return f"Meet {self.name} with {self.side_amount} sides"


class Triangle(Shape):
    def __init__(self, height, s_mount, name):
        print("Here starts Triangle init")
        super().__init__(side_amount=s_mount, name=name)
        self.height = height
        print("Here ends Triangle init")

    def present_triangle(self):
        perimeter = self.side_amount * 3
        area = 0.5 * self.height *
triangle_1 = Triangle(height=5, s_mount=3, name="Triangle")
print(triangle_1.name, triangle_1.side_amount)
print(triangle_1.present())