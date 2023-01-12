# CREAMOS LA CLASE PERSONA CON class
# Los atributos (variables) son nombre y dni y el metodo (funcion) es saludar.

class Persona:
    nombre = "por defecto"
    dni = 0

    def saludar(self):
        print(f"Hola soy {self.nombre}")

inove = Persona() # Crea el objeto que corresponde a la clase Persona
print(inove.nombre) # Muestra el nombre del objeto

inove.nombre = "Fernando" # Cambia el atributo por defecto
print(inove.nombre) # Muestra el nuevo nombre del objeto
inove.saludar() # Retorna el metodo saludar
