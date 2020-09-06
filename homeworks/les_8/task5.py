"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
"""


class Storehouse:
    storage_dict = {}

    def __init__(self, name):
        self.name = name

    def reception(self, equipment, count):
        new_dict = {}
        new_dict[equipment] = count
        self.storage_dict.update(new_dict)

class OfficeEquipment:

    def __init__(self, model, performance, size, wight, height, design, cost):
        self.model = model
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

scan1 = Scanner('1200×1200dpi', 20, 'N1')
scan1.model = 'HP ScanJet Pro 2500'
stor1 = Storehouse('Berlin_055')
print(stor1.name)
stor1.reception(scan1.model, 10)
(print(stor1.storage_dict))