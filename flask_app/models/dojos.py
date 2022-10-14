from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data['idioma']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def guardar(cls, formulario):
        query = "INSERT INTO dojos (nombre, ubicacion, idioma, comentario) VALUES (%(nombre)s, %(ubicacion)s, %(idioma)s, %(comentario)s)"
        result = connectToMySQL('esquema_encuesta_dojo').query_db(query, formulario)
        return result

    @classmethod
    def muestra_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(dojo)
        return dojos

    @staticmethod
    def valida_dojo(formulario):
        is_valid = True
        
        if formulario['nombre'] == '':
            flash('Nombre obligatorio', 'registro')
            is_valid = False

        if formulario['ubicacion'] == '':
            flash('Debes señalar una Locación', 'registro')
            is_valid = False

        if formulario['idioma'] == '':
            flash('Debes señalar un Lenguaje', 'registro')
            is_valid = False

        if formulario['comentario'] == '':
            flash('Comentario obligatorio', 'registro')
            is_valid = False

        return is_valid