class Perro:
    nombre = "Por defecto"
    raza = "Por defecto"
    esperanza_vida = 0

    def ladrar(self):
        print(f'El perro {self.nombre} de raza {self.raza} esta ladrando')


perro_1 = Perro()
print(perro_1.nombre)

perro_1.nombre = 'Nara'
print(perro_1.nombre)

print(perro_1.esperanza_vida)
perro_1.esperanza_vida = '10 años'
print(perro_1.esperanza_vida)
perro_1.ladrar()

perro_2 = Perro()
print(perro_2.nombre)

perro_2.nombre = 'Tomy'
print(perro_2.nombre)

print(perro_2.esperanza_vida)
perro_2.esperanza_vida = '10 años'
print(perro_2.esperanza_vida)
perro_2.ladrar()







