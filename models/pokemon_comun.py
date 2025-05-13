from models.pokemon import Pokemon
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

