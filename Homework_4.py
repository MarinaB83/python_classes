class Rectangle(object):
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
        first = self.is_alike()
        second = other.is_alike()
        is_greater = False
        for perimeter in range(4):
            if self.perimeter_rec() > other.perimeter_rec():
                is_greater = True
                break
        return is_greater


# length = int(input("give a number for length \n "))
# width = int(input("give a number for width \n"))
# obj = Rectangle(length, width)
# print("The perimeter of rec_1 is:", obj.perimeter_rec(), "cm")
# print("The area pf rec_1 is :", obj.area_rec(), "cm^2")
rec_1 = Rectangle(12, 5)
rec_2 = Rectangle(7, 3)
# print(rec_1.area_rec() == rec_2.area_rec())
# print(rec_1.perimeter_rec() > rec_2.perimeter_rec())

# print(rec_1 == rec_2)
print(rec_1 > rec_2)
