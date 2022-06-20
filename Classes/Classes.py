# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

    @temperature.getter
    def temperature(self):
        print("Getting from getter...")
        return self._temperature

    @temperature.deleter
    def temperature(self):
        print("Deleting...")
        del self._temperature

    # getter
    '''
    def get_temperature(self):
        print("Getting value...")
        return self._temperature
    '''
    # setter
    '''
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value
    '''
    # creating a property object
    #temperature = property(get_temperature, set_temperature)


human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())

human.temperature = -273
print(human.temperature)
print(human.to_fahrenheit())
del human.temperature
human = Celsius(5)
human.temperature = 38
print(human.temperature)
