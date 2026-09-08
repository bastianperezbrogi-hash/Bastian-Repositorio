from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py


class Auto(Vehiculo): # Define la clase Auto que hereda de Vehiculo
    def tarifa_hora(self) -> int: # Sobrescribe el método para retornar la tarifa por hora de autos
        return 25000 # Retorna un valor fijo de 25000 para autos
