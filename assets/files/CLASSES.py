'''

    This will hold all the classes for this project

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

class Series:

    def __init__(self, name, desc, img):
        self._name = name
        self._desc = desc
        self._img = img

    def setName(self, name):
        self._name = name
    def setDesc(self, desc):
        self._desc = desc
    def setImg(self, img):
        self._img = img

    def getName(self):
        return self._name
    def getDesc(self):
        return self._desc
    def getImg(self):
        return self._img


