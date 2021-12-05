from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_user():
    client = get_client()
    key = client.key('user')
    return datastore.Entity(key)


class User_manager():
    def find_user(self, email):
        client = get_client()
        query = client.query(kind = 'user')
        query.add_filter("email", "=", email) 
        user = None

        for entity in query.fetch():
            user = entity
        return user

    def register(self, email, password, age, gender):
        user = self.find_user(email)
        if user is not None:
            return "Your email is valid."

        user = create_user()
        user['email'] = email
        user['password'] = password
        user['age'] = age
        user['gender'] = gender
        client = get_client()
        client.put(user)

    def login(self, email, password):
        user = self.find_user(email)
        if user == None:
            return "There is no user associated with this email. Please sign up first."

        if user['password'] != password:
            return "The password is wrong."
        
        return user