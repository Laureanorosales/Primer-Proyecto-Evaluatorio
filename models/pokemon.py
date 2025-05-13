from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, nombre: str, nivel: int, tipo: str, info: str):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__tipo = tipo
        self.__info = info

    def get_nombre(self):
        return self.__nombre

    def get_nivel(self):
        return self.__nivel

    def get_tipo(self):
        return self.__tipo

    def get_info(self):
        return self.__info

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_nivel(self, nivel: int):
        if nivel >= 1:
            self.__nivel = nivel
        else:
            print("El nivel debe ser 1 o mayor.")

    def set_tipo(self, tipo: str):
        self.__tipo = tipo

    def set_info(self, info: str):
        self.__info = info

    def __str__(self):
        return f"{self.get_nombre()} (Nivel {self.get_nivel()}) - Tipo: {self.get_tipo()}. {self.get_info()}"

    def to_dict(self):
        return {
            'nombre': self.get_nombre(),
            'nivel': self.get_nivel(),
            'tipo': self.get_tipo(),
            'info': self.get_info(),
            'categoria': self.__categoria
        }

    @abstractmethod
    def caracteristica_destacada(self):
        pass

    @abstractmethod
    def get_categoria(self):
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass