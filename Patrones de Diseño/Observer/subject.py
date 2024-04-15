class ReactorNuclear:
    def __init__(self):
        # Inicialización de atributos
        self._observers = []  # Lista para almacenar los observadores
        self._temperature = 0  # Inicialización de la temperatura del reactor

    def register_observer(self, observer):
        # Método para registrar un observador
        self._observers.append(observer)  # Agrega el observador a la lista

    def remove_observer(self, observer):
        # Método para eliminar un observador
        self._observers.remove(observer)  # Elimina el observador de la lista

    def notify_observer(self):
        # Método para notificar a los observadores cuando cambia la temperatura
        for observer in self._observers:
            observer.update(self._temperature)  # Llama al método update() en cada observador con la temperatura actual

    def set_temperature(self, temperature):
        # Método para establecer la temperatura del reactor y notificar a los observadores
        self._temperature = temperature  # Actualiza la temperatura del reactor
        self.notify_observer()  # Notifica a los observadores sobre el cambio de temperatura
