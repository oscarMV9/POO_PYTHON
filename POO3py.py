import math

class Circle:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

circulo = Circle(5)
area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
