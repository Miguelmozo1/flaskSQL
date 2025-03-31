from flask_app.config.mysqlconnectioin import connectToMySQL
from flask_app.models.pet import Pet

class Caregiver:
    db = "pet_carers"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.favorite_animal = data["favorite_animal"]
        self.years_active = data["years_active"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.pets = []
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM caregivers;"
        return connectToMySQL(cls.db).query_db(query)
    
    @classmethod
    def create_carer(cls, data):
        query = "INSERT INTO caregivers (first_name, last_name, age, favorite_animal, years_active) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(favorite_animal)s, %(years_active)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        return print(results)
    
    @classmethod
    def carer_pets(cls, data):
        query = "SELECT * FROM caregivers LEFT JOIN pets ON caregivers.id = pets.caregiver_id WHERE caregivers.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        caregiver = cls(results[0])
        for i in results:
            pet = {
                "id": i["pets.id"],
                "name": i["name"],
                "classification": i["classification"],
                "age": i["pets.age"],
                "favorite_toy": i["favorite_toy"],
                "created_at": i["pets.created_at"],
                "updated_at": i["pets.updated_at"]
            }
            caregiver.pets.append(Pet(pet))
        return caregiver


    @classmethod
    def delete_carer(cls, data):
        query = "DELETE FROM caregivers WHERE caregivers.id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)