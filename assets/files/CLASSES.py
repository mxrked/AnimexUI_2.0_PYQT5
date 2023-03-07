'''

    This will hold all the classes and objects

'''

# CLASSES
class Account:
    def __init__(self, username, email, password):
        self._username = username
        self._password = password
        self._email = email

    def setUsername(self, username):
        self._username = username

    def setEmail(self, email):
        self._email = email

    def setPassword(self, password):
        self._password = password

    def getUsername(self):
        return self._username

    def getEmail(self):
        return self._email

    def getPassword(self):
        return self._password

