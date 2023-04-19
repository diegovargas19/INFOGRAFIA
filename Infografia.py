
#1 CLASES
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)

coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Ford", "Mustang")

coche1.mostrar_info()
coche2.mostrar_info()

#2 OBJETOS

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

persona1.mostrar_info()
persona2.mostrar_info()

#3 ATRIBUTOS

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

rectangulo1 = Rectangulo(5, 10)
rectangulo2 = Rectangulo(3, 7)

print("Área del rectángulo 1:", rectangulo1.calcular_area())
print("Área del rectángulo 2:", rectangulo2.calcular_area())

#4 METODOS

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("¡Guau!")

perro1 = Perro("Fido", 3)
perro2 = Perro("Buddy", 5)

perro1.ladrar()
perro2.ladrar()

#5 POLIMORFISMO

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("El perro hace: ¡Guau!")

class Gato(Animal):
    def sonido(self):
        print("El gato hace: ¡Miau!")

#7 ENCAPSULAMIENTO

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print("Titular:", self.__titular)
        print("Saldo:", self.__saldo)

cuenta1 = CuentaBancaria("Juan Pérez", 1000)
cuenta1.mostrar_saldo()

cuenta1._CuentaBancaria__saldo = 2000
cuenta1.mostrar_saldo()

#8 ABSTRACCION

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        print("El coche está acelerando")

    def frenar(self):
        print("El coche está frenando")

class Moto(Vehiculo):
    def acelerar(self):
        print("La moto está acelerando")

    def frenar(self):
        print("La moto está frenando")

coche1 = Coche()
coche1.acelerar()
coche1.frenar()

moto1 = Moto()
moto1.acelerar()
moto1.frenar()



#9 EVENTOS

import tkinter as tk

class VentanaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        self.master.title("Mi Aplicación")
        self.master.geometry("200x200")

        self.boton = tk.Button(self, text="Haz clic", command=self.mostrar_mensaje)
        self.boton.pack()

    def mostrar_mensaje(self):
        print("Se hizo clic en el botón")

root = tk.Tk()
ventana = VentanaPrincipal(root)
ventana.pack()
root.mainloop()




