from flask_app.config.mysqlconnnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result
    
    @classmethod
    def display_one_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        dojo = cls(results[0])
        for r in results:
            na = {
                'id': r['ninjas.id'],
                'first_name': r['first_name'],
                'last_name': r['last_name'],
                'age': r['age'],
                'created_at': r['ninjas.created_at'],
                'updated_at': r['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja(na) )
        return dojo
