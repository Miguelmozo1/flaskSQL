from flask_app.config.mysqlconnectioin import connectToMySQL

class Pet():
    db = "pet_carers"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.classification = data["classification"]
        self.age = data["age"]
        self.favorite_toy = data["favorite_toy"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_pet(cls, data):
        query = "INSERT INTO pets (name, classification, age, favorite_toy, caregiver_id) VALUES (%(name)s, %(classification)s, %(age)s, %(favorite_toy)s, %(caregiver_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
