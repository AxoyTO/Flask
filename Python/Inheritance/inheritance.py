class Vehicle:
    def __init__(self, VIN, weight, manufacturer):
        self.__vin_number = VIN
        self.__weight = weight
        self.__manufacturer = manufacturer

    def GetWeight(self):
        return self.__weight

    def GetManufacturer(self):
        return self.__manufacturer

    def VehicleType(self):
        return "Unknown"

    def __str__(self):
        return "Type: {t}\nVIN Number: {v}\nWeight: {w}\nManufacturer: {m}\nSeats: {s}".format(
            t=self.VehicleType(),
            v=self.__vin_number,
            w=self.__weight,
            m=self.__manufacturer,
            s="Unknown",
        )


class Car(Vehicle):
    def __init__(self, VIN, weight, manufacturer, seats):
        self.__vin_number = VIN
        self.__Vehicle__weight = weight
        self.__Vehicle__manufacturer = manufacturer
        self.__seats = seats

    def NumberOfSeats(self):
        return self.__seats

    def VinNo(self):
        return self.__vin_number

    def GetWeight(self):
        return self.__Vehicle__weight

    def GetManufacturer(self):
        return self.__Vehicle__manufacturer

    def VehicleType(self):
        return "CAR"

    def __str__(self):
        return "Type: {t}\nVIN Number: {v}\nWeight: {w}\nManufacturer: {m}\nSeats: {s}".format(
            t=self.VehicleType(),
            v=self.VinNo(),
            w=self.GetWeight(),
            m=self.GetManufacturer(),
            s=self.NumberOfSeats(),
        )


class Truck(Vehicle):
    def __init__(self, VIN, weight, manufacturer, capacity):
        self.__Vehicle__vin_number = VIN
        self.__Vehicle__weight = weight
        self.__Vehicle__manufacturer = manufacturer
        self.__capacity = capacity

    def VinNo(self):
        return self.__Vehicle__vin_number

    def GetWeight(self):
        return self.__Vehicle__weight

    def GetManufacturer(self):
        return self.__Vehicle__manufacturer

    def NumberOfSeats(self):
        return self.__capacity

    def VehicleType(self):
        return "Truck"


v = Vehicle("42OT", 9000, "LADA")
a = Car("06AY", 1000, "Nissan", 4)
b = Truck("01BCD", 3000, "MAN", 10000)
c = Car("34AT", 1200, "Ford", 4)
d = Truck("09CN", 11000, "Mercedes", 15000)

for k in [v, a, c]:
    print(k, "\n")

for i in [b, d]:
    print(
        "Type: {t}\nVIN Number: {v}\nWeight: {w}\nManufacturer: {m}\nSeats: {s}\n".format(
            t=i.VehicleType(),
            v=i.VinNo(),
            w=i.GetWeight(),
            m=i.GetManufacturer(),
            s=i.NumberOfSeats(),
        )
    )
