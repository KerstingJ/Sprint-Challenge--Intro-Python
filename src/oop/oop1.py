# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    pass


class GroundVehicle(Vehicle):  # inherits from Vehicle
    pass


class FlightVehicle(Vehicle):  # inherits from Vehicle
    pass


class Car(GroundVehicle):  # inherits from GroundVehicle which inherits from Vehicle
    pass


class Motorcycle(GroundVehicle):  # inherits from GroundVehicle which inherits from Vehicle
    pass


class Starship(FlightVehicle):  # inherits from FlightVehicle which inherits from Vehicle
    pass


class Airplane(FlightVehicle):  # inherits from FlightVehicle which inherits from Vehicle
    pass
