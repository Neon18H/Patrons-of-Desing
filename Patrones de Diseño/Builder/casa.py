#se define el objeto
class Casa: 
    def __init__(self):              #<DEFINIMOS EL CONSTRUCTOR, COMPONENTES DE UNA CASA
        self.columns= None           #<DEFINIMOS LOS COMPONENTES
        self.fachada= None
        self.interior = None
    
    def __str__(self) :
        return f'Columns: {self.columns} | Fachada: {self.fachada} | Interior: {self.interior}'
            #RETORNAMOS UNA CADENA FORMATIADA DE TEXTO