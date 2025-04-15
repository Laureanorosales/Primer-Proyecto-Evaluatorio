class Pokemon:
    def __init__(self, nombre: str, nivel: int, tipo: str, info: str):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.info = info

    def __str__(self):
        return f"{self.nombre} (Nivel {self.nivel}) - Tipo: {self.tipo}. {self.info}"

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'nivel': self.nivel,
            'tipo': self.tipo,
            'info': self.info
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['nivel'], data['tipo'], data['info'])
