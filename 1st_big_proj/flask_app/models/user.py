from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data): 
        query = """INSERT INTO users(first_name, last_name, email, password, created_at,updated_at) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, Now(),Now());"""
        return connectToMySQL("magazine_belt_exam").query_db(query, data) 

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("magazine_belt_exam").query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("magazine_belt_exam").query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_one_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL("magazine_belt_exam").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def update(cls,data):
        query = """UPDATE users SET first_name=%(first_name)s,
        last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"""
        return connectToMySQL("magazine_belt_exam").query_db(query,data)
    
    @staticmethod
    def validate_registration(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters.","register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters.","register")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Password and Confirm Password do not match!',"register")
            is_valid = False
        return is_valid