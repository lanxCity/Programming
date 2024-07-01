import math

# ************************** Textbook practices
# Q1.
# ==> Some function
# Fig reformatting
# def fig_reform(amount):
#         amount = str(amount)
#         dec = ''
#
#         if '.' in amount:
#             dec_index = amount.index('.')
#             amount, dec = amount[:dec_index], amount[dec_index:]
#
#         new_set = ''
#         num_reformat = ''
#
#         for i in range(1, len(amount) + 1):
#             new_set = f'{amount[-i]}{new_set}'
#
#             if len(new_set) == 3 and i != len(amount):
#                 num_reformat = f',{new_set}{num_reformat}'
#                 new_set = ''
#
#         num_reformat = f'{new_set}{num_reformat}{dec}'
#
#         return num_reformat
#
#
# # Title: A practical intro....
# # Q2
# class Product:
#     def __init__(self, name, qty, price):
#         self.name = name
#         self._stock_qty = qty
#         self._price = price
#
#     def __str__(self):
#         return f'{self.name}'
#
#     def get_price(self, qty):
#         perc_discount = 0
#
#         if qty < 10:
#             pass
#         elif 10 <= qty < 100:
#             perc_discount += 10
#         else:
#             perc_discount += 20
#
#         discount_amt = (perc_discount / 100) * self._price
#         price = (self._price - discount_amt) * qty
#
#         print(f'{qty} {self.name} -> '
#               f'${fig_reform(self._price)} x {qty}: '
#               f'${fig_reform(price)} ({perc_discount}% discount)')
#
#         return price
#
#     def make_purchase(self, qty):
#         self._stock_qty -= qty
#
#         if qty > self._stock_qty:
#             print('Sorry! Not in stock')
#             return
#
#         self.get_price(qty)
#         print('{:^30s}'.format(f'Added to cart!'))
#
#         return
#
#
# socks = Product('Socks', 100, 5)
# sneakers = Product('Sneaker', 50, 2000)
#
#
# socks.make_purchase(10)
# print()
# sneakers.make_purchase(2)

# Q2.
#
# class Converter:
#     # The list of the available units
#     def __init__(self):
#         self._available_units = ['mm', 'cm', 'm', 'km', 'inch', 'mile', 'yard']
#
#         #Partial conversion
#         self._mm_to_cm = .1
#         self._cm_to_dm = .1
#         self._dm_to_m = .1
#         self._m_to_km = 1 / 1000
#
#         self._mile_to_cm = 160934.4
#         self._inch_to_cm = 2.54
#         self._yard_to_cm = 91.44
#
#     def _valid_data(self, value, init_unit):
#         if init_unit not in self._available_units or value < 0:
#             raise ValueError('Error! Unit not exist or wrong value')
#
#         return True
#
#     @staticmethod
#     def _converted_format(value, pre_conv_value, init_unit, final_unit):
#         answer = value
#         if init_unit != final_unit:
#             answer = value * pre_conv_value
#
#         answer = f'{value}{init_unit} ==> {answer}{final_unit}'
#
#         return answer
#
#     # OR the following
#     # def _converted_format():
#     #         answer = value
#     #         if init_unit != final_unit:
#     #             answer = value * pre_conv_value
#     #
#     #         answer = f'{value}{init_unit} ==> {answer}{final_unit}'
#     #
#     #         return answer
#
#     def _convert_unit(self, value, init_unit, final_unit):
#         if self._valid_data(value, init_unit):
#             pre_conversion = {
#                 'mm': {
#
#                     'cm_to_mm': 1 / self._mm_to_cm,
#                     'm_to_mm': (1 / self._mm_to_cm) * 10**2,
#                     'km_to_mm': (1 / self._m_to_km) * (10 ** 3),
#                     'mile_to_mm': self._mile_to_cm * 10,
#                     'inch_to_mm': self._inch_to_cm * 10,
#                     'yard_to_mm': self._yard_to_cm * 10
#                 },
#                 'cm': {
#                     'mm_to_cm':  self._mm_to_cm,
#                     'm_to_cm': (1 / self._mm_to_cm) * 10,
#                     'km_to_cm': (1 / self._m_to_km) * (10 ** 2),
#                     'mile_to_cm': self._mile_to_cm,
#                     'inch_to_cm': self._inch_to_cm,
#                     'yard_to_cm': self._yard_to_cm
#                 },
#                 'meter': {
#                     'mm_to_m':  (self._mm_to_cm / (10**2)),
#                     'cm_to_m': (self._cm_to_dm / 10),
#                     'km_to_m': 1 / self._m_to_km,
#                     'mile_to_cm': self._mile_to_cm/(10 ** 2),
#                     'inch_to_cm': self._inch_to_cm/(10 ** 2),
#                     'yard_to_cm': self._yard_to_cm/(10 ** 2)
#                 },
#                 'km': {
#                     'mm_to_km': self._mm_to_cm ** 6,
#                     'cm_to_km': self._cm_to_dm * 5,
#                     'm_to_km': self._m_to_km,
#                     'mile_to_km': self._mile_to_cm / (10 ** 5),
#                     'inch_to_km': self._inch_to_cm / (10 ** 5),
#                     'yard_to_km': self._yard_to_cm / (10 ** 5),
#                 },
#                 'inch': {
#                     'mm_to_inch': 1 / (self._inch_to_cm * 10),
#                     'cm_to_inch': 1 / self._inch_to_cm,
#                     'm_to_inch': 1 / (self._cm_to_dm * self._inch_to_cm * .1),
#                     'km_to_inch': ((1 / self._m_to_km) * 100) * self._inch_to_cm,
#                     'mile_to_inch': self._mile_to_cm / self._inch_to_cm,
#                     'yard_to_inch': self._yard_to_cm / self._inch_to_cm,
#                 },
#                 'mile':{
#                     'mm_to_mile': 1 / (self._mile_to_cm * 10),
#                     'cm_to_mile': 1 / self._mile_to_cm,
#                     'm_to_mile': 1 / (self._cm_to_dm * self._mile_to_cm * .1),
#                     'km_to_mile': 1 / (self._m_to_km * self._mile_to_cm * .01),
#                     'inch_to_mile': self._inch_to_cm / self._mile_to_cm,
#                     'yard_to_mile': self._yard_to_cm / self._mile_to_cm,
#                 },
#                 'yard':{
#                     'mm_to_yard': 1 / (self._yard_to_cm * 10),
#                     'cm_to_yard': 1 / self._yard_to_cm,
#                     'm_to_yard': 1 / (self._cm_to_dm * self._yard_to_cm * .1),
#                     'km_to_yard': 1 / (self._m_to_km * self._yard_to_cm * .01),
#                     'inch_to_yard': self._inch_to_cm / self._yard_to_cm,
#                     'yard_to_yard': self._mile_to_cm / self._yard_to_cm,
#                 }
#             }
#
#             final_unit_data = pre_conversion.get(f'{final_unit}')
#             pre_conv_value = final_unit_data.get(f'{init_unit}_to_{final_unit}')
#
#             return self._converted_format(value, pre_conv_value, init_unit, final_unit)
#
#         return
#
#     def millimeter(self, value, init_unit):
#         return self._convert_unit(value, init_unit, 'mm')
#
#     def centimeter(self, value, init_unit):
#         return self._convert_unit(value, init_unit, 'cm')
#
#     def meter(self, value, init_unit):
#         return self._convert_unit(value, init_unit, 'km')
#
#     def kilometer(self, value, init_unit):
#         return self._convert_unit(value, init_unit, 'km')
#
#     def inch(self, value, init_unit):
#         return self._convert_unit(value, init_unit, 'inch')
#
#     def feet(self, value, init_unit):
#         return self._convert_unit(value, init_unit, 'feet')
#
#     def yard(self, value, init_unit):
#         return self._convert_unit(value, init_unit, 'yard')
#
#
# c = Converter()
#
# print(c.inch(0, 'm'))

# ===================> Shape areas calculator
class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        msg = f'The area of the {self.__class__.__name__.lower()} ' \
               f'with sides {self.length} and {self.width} is: ' \
              f'{self._get_area()}'
        return msg

    def __repr__(self):
        return self.__class__.__name__


    def _get_area(self):
        return self.length * self.width

    @classmethod
    def run(cls):
       return


class Rectangle(Shape):
   pass

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Rectangle):
    def __init__(self, height, base):
        super().__init__(height, base)

    def _get_area(self):
        rec_area = super()._get_area()
        return rec_area / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    # def __str__(self):
    #     msg = f'The area of the {self.__class__.__name__.lower()} ' \
    #           f'with radius {self.radius} is: {self._get_area()}'
    #     return msg

    def _get_area(self):
        return math.pi * super()._get_area()


print(Shape(1,2))

# print(Shape.run())