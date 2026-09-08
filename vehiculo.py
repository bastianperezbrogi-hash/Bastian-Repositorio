from abc import ABC, abstractmethod # Importa la clase base ABC y el decorador abstractmethod


class Vehiculo(ABC): # Define la clase abstracta Vehiculo que hereda de ABC
    def __init__(self, patente: str, anio: int): # Constructor que recibe patente y año al crear el objeto
        self.patente = patente # Asigna la patente a través del setter para validar al instanciar el objeto
        self.__anio: int = anio # Asigna el año recibido a un atributo privado
        self.__en_taller: bool = False # Inicializa el estado en False (no está en el taller por defecto) como privado

    @property
    def patente(self) -> str: # Getter que retorna el valor del atributo privado __patente
        return self.__patente # Retorna la patente del vehículo

    @patente.setter
    def patente(self, patente: str) -> None: # Setter que valida y asigna la patente
        if len(patente) < 6 or " " in patente: # Valida que tenga al menos 6 caracteres y no contenga espacios
            raise ValueError("La patente debe tener al menos 6 caracteres y no contener espacios.") # Lanza un ValueError si no cumple los requisitos
        self.__patente = patente # Asigna la patente validada al atributo privado

    @property
    def en_taller(self) -> bool: # Getter de solo lectura para consultar el atributo privado __en_taller
        return self.__en_taller # Retorna si el vehículo se encuentra actualmente en el taller

    def ingresar(self) -> str: # Método para registrar el ingreso del vehículo al taller
        if self.__en_taller: # Verifica si el vehículo ya está marcado como dentro del taller
            return "El vehículo ya se encuentra en el taller." # Devuelve mensaje si ya estaba ingresado
        self.__en_taller = True # Cambia el estado a True (ingresado)
        return "El vehículo ha ingresado al taller." # Devuelve mensaje de éxito

    def entregar(self) -> str: # Método para registrar la salida o entrega del vehículo
        if not self.__en_taller: # Verifica si el vehículo no está en el taller
            return "El vehículo no se encuentra en el taller." # Devuelve mensaje indicando que no se puede entregar
        self.__en_taller = False # Cambia el estado a False (fuera del taller)
        return "El vehículo ha sido entregado." # Devuelve mensaje de éxito

    @abstractmethod
    def tarifa_hora(self) -> int: # Método abstracto para obtener la tarifa por hora
        pass # Método sin implementación que debe ser sobrescrito obligatoriamente por las subclases
