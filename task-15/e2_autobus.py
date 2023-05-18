class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"


class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


bus = Autobus("Renaul Logan", 180, 12)
print(bus.seating_capacity())
