from vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py


class Moto(Vehiculo): # Define la clase Moto que hereda de Vehiculo
    def tarifa_hora(self) -> int: # Sobrescribe el método para retornar la tarifa por hora de motos
        return 15000 # Retorna un valor fijo de 15000 para motos
