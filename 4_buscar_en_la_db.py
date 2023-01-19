# Buscar en la base de datos
# Buscamos en la base de datos y como parametro ponemos el nombre de la clase (clss) en este caso Persona
query = session.query(Persona) # Nos trae toda la info de la base de datos Persona.

persona = query.first() # Guarda en esta variable el primer datos de la consulta anterior.

# Podemos hacer un for para acceder a cada dato y mostrarlo por pantalla.
for persona in query:
    print(persona)

# Para obtener todos los datos de la lista
personas = query.all()
persona = personas[0] # Guarda en esta variable a la primera persona (posicion [0])  

# Filtrar la informacion
# Traer de la tabla Persona todas los datos de la persona cuyo nombre sea 'Inove'
query = session.query(Persona).filter(Persona.name == 'inove')

# Filtrar por varias condiciones
# Filtra por nombre ('inove') y (con este operador &) por edad mayor a 20
query = session.query(Persona).filter(Persona.name == 'inove') & (Persona.age > 20)

""" EJEMPLO """

query = session.query(Persona).filter(Persona.name == 'inove')
persona = query.firsT()
print(persona.name)

""" En la linea 25 trae de la tabla Persona todas la que tengan el nombre 'inove'
    En la linea 26 guarda en la variable la primer persona de la query anterior
    En la linea 27 mustra en pantalla el nombre de la persona de la variable anterior
""" 