import datetime

class Vehiculo:
    def __init__(self, placa, marca, modelo, color):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0
        self.mantenimiento = []

    def tiene_restriccion(self, fecha):
        restriccion_por_dia = {
            0: [1, 2], 
            1: [3, 4],  
            2: [5, 6],  
            3: [7, 8],  
            4: [9, 0], 
            5: [],      
            6: []       
        }
        
        ultimo_digito = int(self.placa[-1])
        
        dia_semana = fecha.weekday()
        
        if ultimo_digito in restriccion_por_dia[dia_semana]:
            return True
        else:
            return False

    def registrar_mantenimiento(self, descripcion, fecha):
        self.mantenimiento.append({'descripcion': descripcion, 'fecha': fecha})
        
    def mostrar_historial_mantenimiento(self):
        return self.mantenimiento
    
    def actualizar_kilometraje(self, km):
        if km > self.kilometraje:
            self.kilometraje = km
        else:
            print("El kilometraje no puede ser menor que el actual.")

    def mostrar_informacion(self):
        return {
            'Placa': self.placa,
            'Marca': self.marca,
            'Modelo': self.modelo,
            'Color': self.color,
            'Kilometraje': self.kilometraje,
            'Mantenimiento': self.mantenimiento
        }

placa_vehiculo = input('ingrese la placa del vehiculo')
vehiculo = Vehiculo(placa_vehiculo, "Toyota", "Corolla", "Rojo")

fecha = datetime.datetime.now()

if vehiculo.tiene_restriccion(fecha):
    print(f"El vehículo con placa {vehiculo.placa} tiene restricción por pico y placa hoy.")
else:
    print(f"El vehículo con placa {vehiculo.placa} no tiene restricción por pico y placa hoy.")

vehiculo.registrar_mantenimiento("Cambio de aceite", "2024-07-27")

vehiculo.actualizar_kilometraje(15000)

print("Historial de mantenimiento:", vehiculo.mostrar_historial_mantenimiento())

print("Información del vehículo:", vehiculo.mostrar_informacion())