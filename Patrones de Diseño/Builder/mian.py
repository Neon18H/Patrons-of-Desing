from construccion import Construccion
from casa_builder import ModernaBuilder, Edificio

construccion = Construccion()                  #llamamos la clase directoria
modern_builder = ModernaBuilder()              
edificio = Edificio()

casa = construccion.make_casa(edificio)
casa2 = construccion.make_casa(modern_builder)

print(casa)
print("  ______________")
print(" /            \\  \\")
print("|   __   __    |  |")
print("|  |__| |__|   |  |")
print("|  |__| |__|   |  |")
print("|              |  |")
print("|    ______    |  |")
print("|   |__  __|   |  |")
print("|   |__||__|   |  |")
print("|              |  |")
print("|    ______    |  |")
print("|   |__  __|   |  |")
print("|   |__||__|   |  |")
print("__________________|")

print(casa2)
print("      /\\")
print("     /--\\")
print("    /----\\")
print("   /------\\")
print("  /--------\\")
print(" /          \\")
print("/------------\\")
print("|    Moderna |")
print("|   Designer |")
print("|      Home  |")
print("|            |")
print("--------------")
