from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app import app
from flask import flash

class Recipe:
    db = "recipes"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under30 = data['under30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creater = None
    
    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under30)s, %(user_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results
    
    @classmethod
    def recipe_by_id(cls, id):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        data = {
            'id': id
            }
        recipe_dictionary = connectToMySQL(cls.db).query_db(query, data)[0]
        recipe_object = Recipe(recipe_dictionary)
        user_obj = user.User({
            "id": recipe_dictionary["users.id"],
            "first_name": recipe_dictionary["first_name"],
            "last_name": recipe_dictionary["last_name"],
            "email": recipe_dictionary["email"],
            "created_at": recipe_dictionary["users.created_at"],
            "updated_at": recipe_dictionary["users.updated_at"]
        })
        recipe_object.user = user_obj
        return recipe_object

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for recipe_dict in results:
            recipe_obj = Recipe(recipe_dict)
            user_obj = user.User({
                "id": recipe_dict["users.id"],
                "first_name": recipe_dict["first_name"],
                "last_name": recipe_dict["last_name"],
                "email": recipe_dict["email"],
                "created_at": recipe_dict["users.created_at"],
                "updated_at": recipe_dict["users.updated_at"]
            })
            recipe_obj.user = user_obj
            recipes.append(recipe_obj)
            return recipes