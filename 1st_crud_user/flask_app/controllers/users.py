from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL("users_schema").query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        results = connectToMySQL("users_schema").query_db(query, data)
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s";
        results = connectToMySQL("users_schema").query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s";
        return connectToMySQL('users_schema').query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s";
        return connectToMySQL('users_schema').query_db(query, data)