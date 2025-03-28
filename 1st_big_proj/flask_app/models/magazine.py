from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Magazine:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def save(cls,data):
        query = """INSERT INTO magazines (title,description,user_id) VALUES (%(title)s,%(description)s, %(user_id)s);"""
        return connectToMySQL("magazine_belt_exam").query_db(query,data)

    @classmethod
    def get_all_w_creator(cls):
        query = """SELECT * FROM magazines JOIN users ON magazines.user_id = users.id;"""
        results = connectToMySQL("magazine_belt_exam").query_db(query)

        magazines = []

        if results:
            for row in results:
                magazine = cls(row)

                data = {
                    'id':row['users.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'email':row['email'],
                    'password':row['password'],
                    'created_at':row['created_at'],
                    'updated_at':row['updated_at']
                }

                magazine.creator = user.User(data)
                magazines.append(magazine)
        return magazines
    
    @classmethod
    def get_one_by_id(cls,data):
        query = "SELECT * FROM magazines WHERE id=%(id)s;"
        results = connectToMySQL("magazine_belt_exam").query_db(query,data)
        return cls(results[0])
    
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM magazines WHERE id=%(id)s"
        return connectToMySQL("magazine_belt_exam").query_db(query,data)
    
    @staticmethod
    def validate_magazine(magazine):
        is_valid = True
        if len(magazine['title']) < 2:
            # flash("Title must be at least 2 characters!", "magazine")
            is_valid = False
        if len(magazine['description']) < 10:
            # flash("description must be at least 10 characters!", "magazine")
            is_valid = False
        return is_valid
    



