class DicConstructor:
    def __init__(self, string):
        self.string = string
        self.dict = {}

    def constructor(self):
        for i in self.string:
            self.dict[i] = 1

        return self.dict

    def remove_duplicate_values(self):
        if not self.dict:
            self.constructor()

        lis_2 = []
        dict =  list(self.dict)
        result = dict()
        for (key, value) in self.d:
            if value not in self.d:
                self.d.append(value)
                result[key] = value
        return result

    def highest_3_values(self):
        if not self.dict:
            self.constructor()
        return sorted(list(self.dict.values()))[-3:]

# str_1 = constructor(input("enter a word\n"), dict())
dict_1 = {"f": 2, "l": 5, "o": 1}
val = dict_1.values()
max_val = max(val)
# print(str_1.creator())
print(max_val)

# HW
class circle:
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius

    def circle_perimeter(self):
        return (2 * self.pi) * self.radius

    def circle_area(self):
        return self.pi * (self.radius ** 2)


circle_1 = circle(3.14, 6)
#
# print("Circle_1 perimeter is: ", circle_1.circle_perimeter(), "\n Circle area is: ", circle_1.circle_area())