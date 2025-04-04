from flask_app.config.mysqlconnnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_ninja_by_id(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])
