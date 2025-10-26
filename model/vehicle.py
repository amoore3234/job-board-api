class Vehicle:
  def __init__(self, number_of_wheels, type_of_tank, sitting_capacity, maximum_velocity):
    self.number_of_wheels = number_of_wheels
    self.type_of_tank = type_of_tank
    self.sitting_capacity = sitting_capacity
    self.maximum_velocity = maximum_velocity

  def number_of_wheels(self):
    return self.number_of_wheels

  def set_number_of_wheels(self, number):
    self.number_of_wheels = number