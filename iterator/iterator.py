class Library:
    def __init__(self, books):
        # Inicializa la biblioteca con una lista de libros
        self.books = books
        
    def __iter__(self):
        # Devuelve una instancia de LibraryIterator para iterar sobre la lista de libros
        return LibraryIterator(self.books)

class LibraryIterator:
    def __init__(self, books):
        # Inicializa el iterador con la lista de libros
        self.books = books
        # Inicializa el índice para realizar el seguimiento de la posición actual en la lista
        self.index = 0
    
    def __next__(self):
        # Verifica si se ha alcanzado el final de la lista de libros
        if self.index == len(self.books):
            # Si es así, lanza StopIteration para indicar el final de la iteración
            raise StopIteration()
        
        # Obtiene el libro actual y lo devuelve
        book = self.books[self.index]
        # Incrementa el índice para apuntar al próximo libro en la lista
        self.index += 1
        return book
    
    def __iter__(self):
        # Devuelve una referencia a sí mismo como el iterador
        return self

# Creamos una instancia de Library con una lista de libros
library = Library(['Python Crash Course', 'Clean Code', 'Design Patterns', 'The Pragmatic Programmer'])
librarymister = Library(['crimen y castigo', 'el visitante', 'la pareja de al aldo', 'catedrales'])

# Creamos un iterador para la biblioteca
iterator = iter(librarymister)

# Iteramos sobre los libros e imprimimos cada uno
while True:
    try:
        # Intenta obtener el siguiente libro del iterador
        current_book = next(iterator)
        # Imprime el libro actual
        print("Libro actual:", current_book)
    except StopIteration:
        # Si se alcanza el final de la lista, se lanza StopIteration y salimos del bucle
        break
