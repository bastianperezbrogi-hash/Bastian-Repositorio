from auto import Auto # Importa la clase Auto desde auto.py
from moto import Moto # Importa la clase Moto desde moto.py
from camion import Camion # Importa la clase Camion desde camion.py

auto1 = Auto("AB1234", 2018) # Instancia un objeto Auto pasándole su patente y año
moto1 = Moto("CD5678", 2020) # Instancia un objeto Moto pasándole su patente y año
camion1 = Camion("EF9012", 2023, 5000) # Instancia un objeto Camion pasándole su patente, año y capacidad de carga en kilos

print(auto1.ingresar()) # Ejecuta ingresar() del auto y muestra el texto retornado en consola
print(moto1.ingresar()) # Ejecuta ingresar() de la moto y muestra el texto retornado en consola
print(camion1.ingresar()) # Ejecuta ingresar() del camión y muestra el texto retornado en consola

print(f"Tarifa por hora del auto: ${auto1.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el auto
print(f"Tarifa por hora de la moto: ${moto1.tarifa_hora()}") # Concatena e imprime la tarifa retornada por la moto
print(f"Tarifa por hora del camión: ${camion1.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el camión

# Demostración de manejo seguro de excepciones al crear objetos (POO Seguro)
try: # Bloque protegido para intentar instanciar un vehículo con datos potencialmente erróneos
    auto_invalido = Auto("A 1", 2022) # Intento de crear un vehículo con patente inválida (longitud menor a 6 y con espacio)
except ValueError as error: # Captura específicamente la excepción de validación lanzada por el setter de patente
    print(f"Registro rechazado de forma segura: {error}") # Muestra el mensaje de error controlado sin detener la ejecución del programa
