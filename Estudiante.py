class Estudiante:
    def __init__(self, nombre, escuela, nota_promedio):
        self.nombre = nombre
        self.escuela = escuela
        self.nota_promedio = nota_promedio

    def on_honor_roll(self):
        if self.nota_promedio >= 12:
            return True
        else:
            return False
