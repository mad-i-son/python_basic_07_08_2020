"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
определить параметры, общие для приведенных типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.
"""


class Storehouse:

    def __init__(self):
        pass


class OfficeEquipment:

    def __init__(self, performance, size, wight, height, design, cost):
        self.performance = performance
        self.size = size
        self.wight = wight
        self.height = height
        self.deign = design
        self.cost = cost


class Printer(OfficeEquipment):

    def __init__(self, principle_image_formation, count_color, connection_interface):
        self.principle_image_formation = principle_image_formation
        self.count_color = count_color
        self.connection_interface = connection_interface


class Scanner(OfficeEquipment):

    def __init__(self, optical_resolution, scanning_speed, sensor_type):
        self.optical_resolution = optical_resolution
        self.scanning_speed = scanning_speed
        self.sensor_type = sensor_type


class Copier(OfficeEquipment):

    def __init__(self, original_and_copy_format, copy_cost):
        self.original_and_copy_format = original_and_copy_format
        self.copy_cost = copy_cost
