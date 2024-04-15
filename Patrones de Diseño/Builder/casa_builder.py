from casa import Casa

class Casabuilder:
    def set_columns(self, columns):
        pass

    def set_fachada(self, fachada):
        pass

    def set_interior(self, interior):
        pass

class ModernaBuilder(Casabuilder):
    def __init__(self):
        self.casa = Casa()
    
    def set_columns(self):
        self.casa.columns = "Rectangular"

    def set_fachada(self):
        self.casa.fachada = "Ligera"
    
    def set_interior(self):
        self.casa.interior = "Panel"

class Edificio(Casabuilder):
    def __init__(self):
        self.casa = Casa()
    
    def set_columns(self):
        self.casa.columns = "Cuadradas"

    def set_fachada(self):
        self.casa.fachada = "Pesada"
    
    def set_interior(self):
        self.casa.interior = "Tradicional"


