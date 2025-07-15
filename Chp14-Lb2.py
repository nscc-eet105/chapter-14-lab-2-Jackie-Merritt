#Jackie-Merritt_Chp14-Lab2_7/14/2025
from dataclasses import dataclass
@dataclass
class computer:

    def __init__(self, cpu_speed = 0, ram_size = 0, drive_size = 0):
        self.__cpu_speed = cpu_speed
        self.__ram_size = ram_size
        self.__drive_size = drive_size
    @property
    def cpu_speed(self):
        return self.__cpu_speed
    @property
    def ram_size(self):
        return self.__ram_size
    @property
    def drive_size(self):
        return self.__drive_size
    @drive_size.setter
    def drive_size(self, drive_size):
        self.__drive_size = drive_size
    @cpu_speed.setter
    def cpu_speed(self, cpu_speed):
        self.__cpu_speed = cpu_speed
    @ram_size.setter
    def ram_size(self, ram_size):
        self.__ram_size = ram_size

    def __str__(self):
        return f'Computer(_Computer__cpu_speed={self.__cpu_speed}, _Computer__ram_size={self.__ram_size}, _Computer__drive_size={self.__drive_size})'


Computer1 = computer(20, 16, 2000)
Computer2 = computer()
Computer2.cpu_speed = 30
Computer2.ram_size = 8
Computer2.drive_size = 4000

print(Computer1)
print(Computer2)
