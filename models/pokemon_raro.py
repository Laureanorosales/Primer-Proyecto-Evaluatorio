from models.pokemon import Pokemon

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