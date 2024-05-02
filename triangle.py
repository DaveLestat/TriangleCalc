from dataclasses import dataclass
import math

@dataclass
class RightTriangle:
    sideA: int
    sideB: int
    
    def __post_init__(self):
        self.sideC = self.calculate_hypotenuse()
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()
        
    def calculate_hypotenuse(self):
        return round(math.sqrt(self.sideA ** 2 + self.sideB ** 2), 3)

    def calculate_area(self):
        return round((self.sideA * self.sideB) / 2, 3)

    def calculate_perimeter(self):
        return round(self.sideA + self.sideB + self.sideC, 3)