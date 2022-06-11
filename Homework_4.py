class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter_rec(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def area_rec(self):
        area = self.length * self.width
        return area

    def is_alike(self, other):
        a = float(self.area_rec() / other.area_rec())
        b = float(self.perimeter_rec() / other.perimeter_rec())
        is_alike = True

        if a != b:
            return False
        return is_alike


# length = int(input("give a number for length \n "))
# width = int(input("give a number for width \n"))
# obj = Rectangle(length, width)
# print("The perimeter of rec_1 is:", obj.perimeter_rec(), "cm")
# print("The area of rec_1 is :", obj.area_rec(), "cm^2")
rec_1 = Rectangle(12, 5)
rec_2 = Rectangle(7, 3)
# print(rec_1.area_rec() == rec_2.area_rec())
# print(rec_1.perimeter_rec() == rec_2.perimeter_rec())
# print(rec_1.is_alike == rec_2.is_alike)
# print(rec_1.area_rec() > rec_2.area_rec())
# print(rec_1 > rec_2)
