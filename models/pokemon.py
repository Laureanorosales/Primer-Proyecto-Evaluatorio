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

# ----Subclases - Herencia ----


class PokemonComun(Pokemon):
    def __init__(self, nombre: str, nivel: int, tipo: str, info: str):
        super().__init__(nombre, nivel, tipo, info)
        self.__categoria = 'Comun'

    def get_nombre(self):
        return super().get_nombre()

    def get_categoria(self):
        return self.__categoria

    def __str__(self):
        base_str = super().__str__()
        return f'{base_str} - Categoría: {self.__categoria}'

    def caracteristica_destacada(self):
        return f"{self.get_nombre()} es un Pokémon común, sin habilidades destacadas."

    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['nivel'], data['tipo'], data['info'])

    def to_dict(self):
        return {
            'nombre': self.get_nombre(),
            'nivel': self.get_nivel(),
            'tipo': self.get_tipo(),
            'info': self.get_info(),
            'categoria': self.get_categoria()
        }

# Subclase Pokemon raro (Hereda clase abstracta Pokemon (nombre, nivel, tipo, info) y agrega rarezal(que lo convierte en raro a este pokemon))


class PokemonRaro(Pokemon):
    def __init__(self, nombre: str, nivel: int, tipo: str, info: str, rareza: str, poder_especial: str):
        super().__init__(nombre, nivel, tipo, info)
        self.__categoria = 'Raro'
        self.__rareza = rareza

    def get_nombre(self):
        return super().get_nombre()

    def get_categoria(self):
        return self.__categoria

    def get_rareza(self):
        return self.__rareza

    def __str__(self):

        base_str = super().__str__()
        return f"{base_str} - Categoría: {self.__categoria} - Rareza: {self.__rareza}"

    def caracteristica_destacada(self):
        return f"{self.get_nombre()} destaca por su rareza: {self.__rareza}."

    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['nivel'], data['tipo'], data['info'], data['rareza'])

    def to_dict(self):
        return {
            'nombre': self.get_nombre(),
            'nivel': self.get_nivel(),
            'tipo': self.get_tipo(),
            'info': self.get_info(),
            'categoria': self.get_categoria(),
            'rareza': self.get_rareza()
        }
# Subclase Pokemon Legendario (Hereda clase abstracta Pokemon (nombre, nivel, tipo, info) y agrega poder especial(caracteristica de un pokemon legendario))


class PokemonLegendario(Pokemon):
    def __init__(self, nombre: str, nivel: int, tipo: str, info: str, poder_especial: str):
        super().__init__(nombre, nivel, tipo, info)
        self.__categoria = "Legendario"
        self.__poder_especial = poder_especial

    def get_nombre(self):
        return super().get_nombre()

    def get_categoria(self):
        return self.__categoria

    def get_poder_especial(self):
        return self.__poder_especial

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} - Categoría: {self.__categoria} - Poder especial: {self.__poder_especial}"

    def caracteristica_destacada(self):
        return f"{self.get_nombre()} es legendario y posee el poder especial: {self.__poder_especial}."

    # Agregando from-dict, porque Pokemon siendo abstracto no se puede llamar
    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['nivel'], data['tipo'], data['info'], data['poder_especial'])

    def to_dict(self):
        return {
            'nombre': self.get_nombre(),
            'nivel': self.get_nivel(),
            'tipo': self.get_tipo(),
            'info': self.get_info(),
            'categoria': self.get_categoria(),
            'poder_especial': self.get_poder_especial()
        }
