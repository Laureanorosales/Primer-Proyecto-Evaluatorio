from models.pokemon import Pokemon
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
