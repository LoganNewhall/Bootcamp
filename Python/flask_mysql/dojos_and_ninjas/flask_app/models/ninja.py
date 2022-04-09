from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
            query = "SELECT * FROM ninjas;"
            # make sure to call the connectToMySQL function with the schema you are targeting.
            results = connectToMySQL('dojos_and_ninjas').query_db(query)
            # Create an empty list to append our instances of friends
            ninjas = []
            # Iterate over the db results and create instances of friends with cls.
            for ninja in results:
                ninjas.append( cls(ninja) )
            return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (f_name, l_name, age, dojo_id, created_at, updated_at) VALUES (%(f_name)s, %(l_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data ) 