#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///secundaria.db")
base = declarative_base()


class Tutor(base):
    __tablename__ = "tutor"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return f"Tutor: {self.name}"

class Estudiante(base):
    __tablename__ = "estudiante"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Integer)
    tutor_id = Column(Integer, ForeignKey("tutor.id"))

    tutor = relationship("Tutor")

    def __repr__(self):
        return f"Estudiante: {self.name}, edad {self.age}, grado {self.grade}, tutor {self.tutor.name}"

def create_schema():
    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos
    base.metadata.drop_all(engine)

    # Crear las tablas
    base.metadata.create_all(engine)

def fill():
    print('Completemos esta tablita!')

    Session = sessionmaker(bind=engine)
    session = Session()


    # Llenar la tabla de la secundaria con al munos 2 tutores
    # Cada tutor tiene los campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del tutor (puede ser solo nombre sin apellido)

    tutor_1 = Tutor(name= 'Ricardo')
    tutor_2 = Tutor(name= 'Jose')

    session.add(tutor_1)
    session.add(tutor_2)

    session.commit()    

    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> el tutor de ese estudiante (el objeto creado antes)

    estudiante_1 = Estudiante(name='Emmanuel', age='39', grade=6, tutor=tutor_1)
    estudiante_2 = Estudiante(name='Fernando', age='22', grade=6, tutor=tutor_1)
    estudiante_3 = Estudiante(name='Cristian', age='29', grade=2, tutor=tutor_2)
    estudiante_4 = Estudiante(name='Facundo', age='28', grade=2, tutor=tutor_1)
    estudiante_5 = Estudiante(name='Marcelo', age='30', grade=3, tutor=tutor_2)

    session.add_all(estudiante_1, estudiante_2, estudiante_3, estudiante_4, estudiante_5)
    session.commit()

    # No olvidarse que antes de poder crear un estudiante debe haberse
    # primero creado el tutor.

def fetch():
    print('Comprovemos su contenido, ¿qué hay en la tabla?')

    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear una query para imprimir en pantalla
    # todos los objetos creaods de la tabla estudiante.
    
    query = session.query(Estudiante)
           
    # Imprimir en pantalla cada objeto que traiga la query
    # Realizar un bucle para imprimir de una fila a la vez

    for querys in query:
        print(querys)

def search_by_tutor(tutor):
    print('Operación búsqueda!')

    Session = sessionmaker(bind=engine)
    session = Session()

    # Esta función recibe como parámetro el nombre de un posible tutor.
    # Crear una query para imprimir en pantalla
    # aquellos estudiantes que tengan asignado dicho tutor.

    # Para poder realizar esta query debe usar join, ya que
    # deberá crear la query para la tabla estudiante pero
    # buscar por la propiedad de tutor.name
 
    query = session.query(Estudiante).join(Estudiante.tutor).filter(Tutor.name == tutor)

    print('Los siguientes estudiantes cursan con el tutor buscado')

    for estudiante in query:
        
        print(estudiante)

def modify(id, name):
    print('Modificando la tabla')

    Session = sessionmaker(bind=engine) 
    session = Session()

    # Deberá actualizar el tutor de un estudiante, cambiarlo para eso debe
    # 1) buscar con una query el tutor por "tutor.name" usando name
    # pasado como parámetro y obtener el objeto del tutor
    # 2) buscar con una query el estudiante por "estudiante.id" usando
    # el id pasado como parámetro
    # 3) actualizar el objeto de tutor del estudiante con el obtenido
    # en el punto 1 y actualizar la base de datos

    # TIP: En clase se hizo lo mismo para las nacionalidades con
    # en la función update_persona_nationality

    query = session.query(Tutor).filter(Tutor.name == name)
    tutor = query.first()
    print(tutor)
    
    

    query = session.query(Estudiante).filter(Estudiante.id == id)
    estudiante = query.first()
    
    estudiante.tutor = tutor

    session.add(estudiante)
    session.commit()

    print(f'El estudiante {estudiante} fue actualizado.')

def count_grade(grade):
    print('Estudiante por grado')
    # Utilizar la sentencia COUNT para contar cuantos estudiante
    # se encuentran cursando el grado "grade" pasado como parámetro
    # Imprimir en pantalla el resultado

    # TIP: En clase se hizo lo mismo para las nacionalidades con
    # en la función count_persona

    Session = sessionmaker(bind=engine) 
    session = Session()

    result = session.query(Estudiante).filter(Estudiante.grade == grade).count()
    #cuenta = result.first()

    print(f'Personas de {grade} grado encontradas: {result}')

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    fill()
    fetch()

    tutor = 'Jose'
    search_by_tutor(tutor)

    nuevo_tutor = 'Ricardo'
    id = 2
    modify(id, nuevo_tutor)

    grade = 2
    count_grade(grade)
