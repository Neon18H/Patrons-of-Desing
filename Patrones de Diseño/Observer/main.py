from subject import ReactorNuclear
from observer import TemperatureDisplay

def main():
    reactor_nuclear = ReactorNuclear()  # Crear una instancia de ReactorNuclear
    temperature_display = TemperatureDisplay()  # Crear una instancia de TemperatureDisplay
    

    reactor_nuclear.register_observer(temperature_display)
    reactor_nuclear.set_temperature(10)
    reactor_nuclear.set_temperature(20)
    reactor_nuclear.set_temperature(30)

if __name__ == "__main__":
    main()
