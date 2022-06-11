# Ex1
class Person(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def present(self):
        return f"Person {self.name} {self.surname}"


class Student(Person):
    def __init__(self, nationality, age, s_name, s_surname):
        super().__init__(s_name, s_surname)
        self.nationality = nationality
        self.age = age

    def present_student(self):
        return f"Meet {self.nationality} {self.age} {super().present()}"


student_1 = Student("John", "David", "British student", 25)
print(student_1)
print(student_1.present_student())


# Ex2
class Country(object):
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

    def present_country(self):
        return f" The Country {self.name} is in this {self.continent}"


class Brand(object):
    def __init__(self, b_name, b_start_date):
        self.b_name = b_name
        self.b_date = b_start_date

    def present_brand(self):
        return f"This Brand {self.b_name} starts at {self.b_date}"


class Season(object):
    def __init__(self, s_name, avg_temp):
        self.s_name = s_name
        self.avg_temp = avg_temp

    def present_season(self):
        return f" In this Season {self.s_name }, the weather  will be at {self.avg_temp} degrees celsius "


class Product(Country, Brand, Season):
    def __init__(self, p_name, p_type, p_price, p_quantity, discount_percentage, discount_amount, discounted_price,
                 name, continent, b_name, b_start_date, s_name, avg_temp):
        Country.__init__(self, name, continent)
        Brand.__init__(self, b_name, b_start_date)
        Season.__init__(self, s_name, avg_temp)
        self.p_name = p_name
        self.p_type = p_type
        self.p_price = p_price
        self.p_quantity = p_quantity
        self.disc_percentage = discount_percentage
        self.discount_amount = discount_amount
        self.discounted_price = discounted_price
        self.total_price = self.p_price * self.p_quantity

    def present_product(self):
        return f"Product {self.p_name} with {self.p_type}, for one piece cost is {self.p_price} dollar,for {self.p_quantity} pieces is {self.total_price} dollar"

    def discount_product(self):
        self.discount_amount = (self.p_price * self.disc_percentage) / 100
        self.discounted_price = (self.p_price - self.discount_amount)

        return f"Product will  discount {self.discount_amount} dollars, the price will be after discount is {self.discounted_price} "

    def increase(self):
        self.p_quantity += 1
        return f"Product quantity after increasing is {self.p_quantity}"

    def decrease(self):
        self.p_quantity -= 1
        return f"Product quantity after decreasing is {self.p_quantity}"


product_1 = Product("coffee", "drink", 40, 5, 10, 12, 10, "mr drink", "Asian", "hot drink", 2020, "chocolate", 5)
print(product_1.present_product())
print(product_1.discount_product())
print(product_1.increase())
print(product_1.decrease())


# Ex3
class Hotel(object):
    def __init__(self, h_name, h_place, room_mid, mid_r_price, room_lux, l_r_price):
        self.h_name = h_name
        self.h_place = h_place
        self.room_mid = room_mid
        self.mid_r_price = mid_r_price
        self.room_lux = room_lux
        self.l_r_price = l_r_price

    def present_hotel(self):
        return f"The hotel {self.h_name }, which located in {self.h_place}, it has two different rooms {self.room_mid}"\
               f"which price is {self.mid_r_price},and the other one is {self.room_lux}, which price is{self.l_r_price}"


class Taxi(object):
    def __init__(self, t_name, car_types, price_for_trip, discount_percentage, discount_amount, discount_value):
        self.t_name = t_name
        self.car_types = car_types
        self.price_for_trip = price_for_trip
        self.disc_percentage = discount_percentage
        self.discount_amount = discount_amount
        self.discount_value = discount_value

    def present_taxi(self):
        self.discount_amount = self.price_for_trip * self.disc_percentage
        self.discount_value = self.price_for_trip - self.discount_amount
        return f"The company {self.t_name} which has {self.car_types} is offer you {self.price_for_trip}, " \
               f"it will make discount {self.discount_amount}, you will pay after discount {self.discount_value}"


class Tour(Hotel, Taxi):
    def __init__(self, tour_name,  h_name, h_place, room_mid, mid_r_price, room_lux, l_r_price, t_name, car_types,
                 price_for_trip, discount_percentage, discount_amount, discount_value):
        Hotel. __init__(self, h_name, h_place, room_mid, mid_r_price, room_lux, l_r_price)
        Taxi. __init__(self, t_name, car_types, price_for_trip, discount_percentage, discount_amount, discount_value)
        self.tour_name = tour_name
        self.price_mid = (mid_r_price + price_for_trip)
        self.price_lux = (l_r_price + price_for_trip)

    def global_present(self):
        return f"Hello we offer you {self.tour_name} we have two options{self.price_mid}and {self.price_lux} which " \
               f"includes transport with {self.t_name} company , which provides {self.car_types} cars and price"\
               f"for it is {self.price_for_trip}, we will stay at {self.h_name},which offers two types of rooms " \
               f"{self.mid_r_price} and {self.l_r_price} AMD "

#
# room_mid = {r1: free, r2: free, r3: free}
# room_lux = {r1: free, r2: busy, r3: busy}
# hotel_1 = Hotel("Le Ran", "Geghard", room_mid, 10000, room_lux, 20000)
